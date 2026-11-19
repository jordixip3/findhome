"""
LookingForHome — Database Layer (MySQL & SQLite Multi-Engine)
Supports native MySQL / MariaDB (via PyMySQL) for production environments,
with automatic graceful fallback to SQLite for local development or testing.
Includes direct landlord/agency contact metadata on all property listings.
"""

import os
import json
import uuid
from datetime import datetime, timezone
from typing import List, Dict, Any, Optional

# Database Engine Configuration
DB_TYPE_ENV = os.getenv("DB_TYPE", "").strip().lower()
MYSQL_HOST = os.getenv("MYSQL_HOST", "127.0.0.1")
MYSQL_PORT = int(os.getenv("MYSQL_PORT", "3306"))
MYSQL_USER = os.getenv("MYSQL_USER", "lookingforhome")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "LookingForHome2026!")
MYSQL_DB = os.getenv("MYSQL_DB", "lookingforhome")

SQLITE_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "findhome.db")

_ACTIVE_ENGINE = None


def detect_engine() -> str:
    global _ACTIVE_ENGINE
    if _ACTIVE_ENGINE is not None:
        return _ACTIVE_ENGINE

    if DB_TYPE_ENV == "sqlite":
        _ACTIVE_ENGINE = "sqlite"
        return _ACTIVE_ENGINE

    # Try connecting to MySQL if DB_TYPE_ENV is "mysql" or unspecified
    try:
        import pymysql
        conn = pymysql.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DB,
            connect_timeout=3
        )
        conn.close()
        _ACTIVE_ENGINE = "mysql"
        return _ACTIVE_ENGINE
    except Exception:
        # Fallback to SQLite if MySQL is unavailable
        _ACTIVE_ENGINE = "sqlite"
        return _ACTIVE_ENGINE


def get_raw_connection():
    engine = detect_engine()
    if engine == "mysql":
        import pymysql
        import pymysql.cursors
        conn = pymysql.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DB,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=False
        )
        return "mysql", conn
    else:
        import sqlite3
        conn = sqlite3.connect(SQLITE_PATH)
        conn.row_factory = sqlite3.Row
        return "sqlite", conn


class DBContext:
    def __init__(self):
        self.engine, self.conn = get_raw_connection()
        self.cursor = self.conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if exc_type is None:
                self.conn.commit()
            else:
                self.conn.rollback()
        finally:
            self.cursor.close()
            self.conn.close()

    def execute(self, sql: str, params: Optional[tuple] = None):
        target_sql = sql
        if self.engine == "mysql":
            target_sql = sql.replace("?", "%s")
        if params is not None:
            return self.cursor.execute(target_sql, params)
        return self.cursor.execute(target_sql)

    def fetchall(self) -> List[Dict[str, Any]]:
        rows = self.cursor.fetchall()
        if not rows:
            return []
        if self.engine == "mysql":
            return list(rows)
        return [dict(r) for r in rows]

    def fetchone(self) -> Optional[Dict[str, Any]]:
        row = self.cursor.fetchone()
        if not row:
            return None
        if self.engine == "mysql":
            return dict(row)
        return dict(row)

    def fetchval(self) -> Any:
        row = self.cursor.fetchone()
        if not row:
            return None
        if isinstance(row, dict):
            return list(row.values())[0]
        return row[0]


def init_db():
    engine = detect_engine()

    with DBContext() as db:
        if db.engine == "mysql":
            # 1. Properties
            db.execute("""
            CREATE TABLE IF NOT EXISTS properties (
                id VARCHAR(64) PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                description TEXT,
                city VARCHAR(100) NOT NULL,
                country VARCHAR(100) NOT NULL,
                address VARCHAR(255) NOT NULL,
                latitude DOUBLE NOT NULL,
                longitude DOUBLE NOT NULL,
                total_rent DOUBLE NOT NULL,
                ideal_roommates INT NOT NULL,
                rent_per_person DOUBLE NOT NULL,
                bedrooms INT NOT NULL,
                bathrooms INT NOT NULL,
                surface_sqm INT NOT NULL,
                property_type VARCHAR(50) DEFAULT 'piso',
                has_elevator TINYINT(1) DEFAULT 1,
                is_exterior TINYINT(1) DEFAULT 1,
                is_furnished TINYINT(1) DEFAULT 1,
                has_terrace TINYINT(1) DEFAULT 0,
                has_air_con TINYINT(1) DEFAULT 0,
                energy_rating VARCHAR(10) DEFAULT 'B',
                source_portal VARCHAR(100) DEFAULT 'Open Portal',
                source_url VARCHAR(500),
                images MEDIUMTEXT,
                contact_name VARCHAR(120) DEFAULT 'Inmobiliaria / Propietario Directo',
                contact_phone VARCHAR(50) DEFAULT '+34 600 123 456',
                contact_email VARCHAR(120) DEFAULT 'contacto@lookingforhome.duckdns.org',
                contact_whatsapp VARCHAR(50) DEFAULT '34600123456',
                status VARCHAR(50) DEFAULT 'available',
                created_at VARCHAR(100) NOT NULL
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
            """)

            # 2. Users
            db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id VARCHAR(64) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) UNIQUE NOT NULL,
                phone VARCHAR(50) NOT NULL,
                age INT,
                occupation VARCHAR(255),
                budget_max DOUBLE NOT NULL,
                preferred_city VARCHAR(100) NOT NULL,
                preferred_roommates INT DEFAULT 4,
                bio TEXT,
                languages MEDIUMTEXT,
                created_at VARCHAR(100) NOT NULL
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
            """)

            # 3. Communities
            db.execute("""
            CREATE TABLE IF NOT EXISTS communities (
                id VARCHAR(64) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                property_id VARCHAR(64),
                city VARCHAR(100) NOT NULL,
                max_members INT NOT NULL,
                description TEXT,
                created_by_user_id VARCHAR(64),
                status VARCHAR(50) DEFAULT 'forming',
                created_at VARCHAR(100) NOT NULL
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
            """)

            # 4. Community Members
            db.execute("""
            CREATE TABLE IF NOT EXISTS community_members (
                id VARCHAR(64) PRIMARY KEY,
                community_id VARCHAR(64) NOT NULL,
                user_id VARCHAR(64) NOT NULL,
                role VARCHAR(50) DEFAULT 'member',
                rent_share DOUBLE,
                fee_paid TINYINT(1) DEFAULT 0,
                joined_at VARCHAR(100) NOT NULL
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
            """)

            # 5. Inquiries
            db.execute("""
            CREATE TABLE IF NOT EXISTS inquiries (
                id VARCHAR(64) PRIMARY KEY,
                property_id VARCHAR(64) NOT NULL,
                user_name VARCHAR(255) NOT NULL,
                user_email VARCHAR(255) NOT NULL,
                user_phone VARCHAR(50) NOT NULL,
                message TEXT NOT NULL,
                community_id VARCHAR(64),
                created_at VARCHAR(100) NOT NULL
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
            """)

            # 6. Access Logs (Visitor IP & Geolocation Analytics)
            db.execute("""
            CREATE TABLE IF NOT EXISTS access_logs (
                id VARCHAR(64) PRIMARY KEY,
                ip VARCHAR(64) NOT NULL,
                country VARCHAR(100) DEFAULT 'Desconocido',
                country_code VARCHAR(10) DEFAULT 'UN',
                region VARCHAR(100) DEFAULT '',
                city VARCHAR(100) DEFAULT 'Desconocido',
                latitude DOUBLE DEFAULT 0.0,
                longitude DOUBLE DEFAULT 0.0,
                path VARCHAR(255) DEFAULT '/',
                method VARCHAR(10) DEFAULT 'GET',
                status_code INT DEFAULT 200,
                user_agent VARCHAR(500) DEFAULT '',
                device_type VARCHAR(50) DEFAULT 'Desktop',
                referrer VARCHAR(500) DEFAULT '',
                created_at VARCHAR(100) NOT NULL
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
            """)
        else:
            # SQLite Tables
            db.execute("""
            CREATE TABLE IF NOT EXISTS properties (
                id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT,
                city TEXT NOT NULL,
                country TEXT NOT NULL,
                address TEXT NOT NULL,
                latitude REAL NOT NULL,
                longitude REAL NOT NULL,
                total_rent REAL NOT NULL,
                ideal_roommates INTEGER NOT NULL,
                rent_per_person REAL NOT NULL,
                bedrooms INTEGER NOT NULL,
                bathrooms INTEGER NOT NULL,
                surface_sqm INTEGER NOT NULL,
                property_type TEXT DEFAULT 'piso',
                has_elevator INTEGER DEFAULT 1,
                is_exterior INTEGER DEFAULT 1,
                is_furnished INTEGER DEFAULT 1,
                has_terrace INTEGER DEFAULT 0,
                has_air_con INTEGER DEFAULT 0,
                energy_rating TEXT DEFAULT 'B',
                source_portal TEXT DEFAULT 'Open Portal',
                source_url TEXT,
                images TEXT,
                contact_name TEXT DEFAULT 'Inmobiliaria / Propietario Directo',
                contact_phone TEXT DEFAULT '+34 600 123 456',
                contact_email TEXT DEFAULT 'contacto@lookingforhome.duckdns.org',
                contact_whatsapp TEXT DEFAULT '34600123456',
                status TEXT DEFAULT 'available',
                created_at TEXT NOT NULL
            )
            """)

            db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                phone TEXT NOT NULL,
                age INTEGER,
                occupation TEXT,
                budget_max REAL NOT NULL,
                preferred_city TEXT NOT NULL,
                preferred_roommates INTEGER DEFAULT 4,
                bio TEXT,
                languages TEXT,
                created_at TEXT NOT NULL
            )
            """)

            db.execute("""
            CREATE TABLE IF NOT EXISTS communities (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                property_id TEXT,
                city TEXT NOT NULL,
                max_members INTEGER NOT NULL,
                description TEXT,
                created_by_user_id TEXT,
                status TEXT DEFAULT 'forming',
                created_at TEXT NOT NULL,
                FOREIGN KEY (property_id) REFERENCES properties(id),
                FOREIGN KEY (created_by_user_id) REFERENCES users(id)
            )
            """)

            db.execute("""
            CREATE TABLE IF NOT EXISTS community_members (
                id TEXT PRIMARY KEY,
                community_id TEXT NOT NULL,
                user_id TEXT NOT NULL,
                role TEXT DEFAULT 'member',
                rent_share REAL,
                fee_paid INTEGER DEFAULT 0,
                joined_at TEXT NOT NULL,
                FOREIGN KEY (community_id) REFERENCES communities(id),
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
            """)

            db.execute("""
            CREATE TABLE IF NOT EXISTS inquiries (
                id TEXT PRIMARY KEY,
                property_id TEXT NOT NULL,
                user_name TEXT NOT NULL,
                user_email TEXT NOT NULL,
                user_phone TEXT NOT NULL,
                message TEXT NOT NULL,
                community_id TEXT,
                created_at TEXT NOT NULL
            )
            """)

            db.execute("""
            CREATE TABLE IF NOT EXISTS access_logs (
                id TEXT PRIMARY KEY,
                ip TEXT NOT NULL,
                country TEXT DEFAULT 'Desconocido',
                country_code TEXT DEFAULT 'UN',
                region TEXT DEFAULT '',
                city TEXT DEFAULT 'Desconocido',
                latitude REAL DEFAULT 0.0,
                longitude REAL DEFAULT 0.0,
                path TEXT DEFAULT '/',
                method TEXT DEFAULT 'GET',
                status_code INTEGER DEFAULT 200,
                user_agent TEXT DEFAULT '',
                device_type TEXT DEFAULT 'Desktop',
                referrer TEXT DEFAULT '',
                created_at TEXT NOT NULL
            )
            """)

            # Ensure columns exist in SQLite if upgrading existing database
            db.execute("PRAGMA table_info(properties)")
            existing_cols = [r["name"] if isinstance(r, dict) else r[1] for r in db.fetchall()]
            if "property_type" not in existing_cols:
                db.execute("ALTER TABLE properties ADD COLUMN property_type TEXT DEFAULT 'piso'")
            if "contact_name" not in existing_cols:
                db.execute("ALTER TABLE properties ADD COLUMN contact_name TEXT DEFAULT 'Inmobiliaria / Propietario Directo'")
            if "contact_phone" not in existing_cols:
                db.execute("ALTER TABLE properties ADD COLUMN contact_phone TEXT DEFAULT '+34 600 123 456'")
            if "contact_email" not in existing_cols:
                db.execute("ALTER TABLE properties ADD COLUMN contact_email TEXT DEFAULT 'contacto@lookingforhome.duckdns.org'")
            if "contact_whatsapp" not in existing_cols:
                db.execute("ALTER TABLE properties ADD COLUMN contact_whatsapp TEXT DEFAULT '34600123456'")

        # Check if properties exist
        db.execute("SELECT COUNT(*) FROM properties")
        if db.fetchval() == 0:
            _seed_database(db)
        else:
            # Refresh local photos and contact info for all properties if needed
            _update_seed_contact_info(db)

        # Feed & sync open portals properties to ensure high variety
        try:
            from app.services.portal_feeder import feed_open_portal_properties
            feed_open_portal_properties(db)
        except Exception as e:
            print(f"[PortalFeeder] Notice while feeding open portals: {e}")

        # Check if access_logs has initial seed data
        try:
            db.execute("SELECT COUNT(*) FROM access_logs")
            if db.fetchval() == 0:
                _seed_access_logs(db)
        except Exception as e:
            print(f"[AccessLogs] Notice while checking access logs: {e}")


def _seed_database(db: DBContext):
    now = datetime.now(timezone.utc).isoformat()

    properties = [
        # Madrid
        {
            "id": "prop-mad-01",
            "title": "Ático luminoso con terraza en Malasaña — Ideal para 4 personas",
            "description": "Gran piso reformado en pleno centro de Madrid. 4 habitaciones independientes amplias con armarios empotrados, salón exterior con luz natural todo el día, 2 baños completos y cocina equipada. Edificio con ascensor.",
            "city": "Madrid",
            "country": "España",
            "address": "Calle del Pez, 28, Malasaña, 28004 Madrid",
            "latitude": 40.4238,
            "longitude": -3.7065,
            "total_rent": 1800.0,
            "ideal_roommates": 4,
            "bedrooms": 4,
            "bathrooms": 2,
            "surface_sqm": 125,
            "property_type": "atico",
            "has_elevator": 1,
            "is_exterior": 1,
            "is_furnished": 1,
            "has_terrace": 1,
            "has_air_con": 1,
            "energy_rating": "A",
            "source_portal": "Idealista",
            "source_url": "https://www.idealista.com",
            "images": ["static/images/prop-mad-01-1.jpg", "static/images/prop-mad-01-2.jpg", "static/images/prop-mad-01-3.jpg", "static/images/prop-mad-01-4.jpg"],
            "contact_name": "Carlos Mendoza (Propietario Directo)",
            "contact_phone": "+34 611 223 344",
            "contact_email": "carlos.mendoza.mad@gmail.com",
            "contact_whatsapp": "34611223344"
        },
        {
            "id": "prop-mad-02",
            "title": "Piso señorial en Chamberí — 5 dormitorios y 3 baños",
            "description": "Excelente vivienda para minicomunidad joven de 5 profesionales o estudiantes. Techos altos, calefacción central, exterior a calle ajardinada, 3 baños para máxima comodidad y cocina office.",
            "city": "Madrid",
            "country": "España",
            "address": "Calle Santa Engracia, 84, Chamberí, 28010 Madrid",
            "latitude": 40.4371,
            "longitude": -3.7002,
            "total_rent": 2250.0,
            "ideal_roommates": 5,
            "bedrooms": 5,
            "bathrooms": 3,
            "surface_sqm": 155,
            "property_type": "piso",
            "has_elevator": 1,
            "is_exterior": 1,
            "is_furnished": 1,
            "has_terrace": 0,
            "has_air_con": 1,
            "energy_rating": "B",
            "source_portal": "Inmobiliaria Chamberí Siglo XXI",
            "source_url": "https://www.fotocasa.es",
            "images": ["static/images/prop-mad-02-1.jpg", "static/images/prop-mad-02-2.jpg", "static/images/prop-mad-02-3.jpg", "static/images/prop-mad-02-4.jpg"],
            "contact_name": "Inmobiliaria Chamberí Siglo XXI",
            "contact_phone": "+34 914 556 789",
            "contact_email": "alquileres@chamberisigloxxi.es",
            "contact_whatsapp": "34622334455"
        },
        {
            "id": "prop-mad-03",
            "title": "Loft moderno cerca de Madrid Río — 3 habitaciones dobles",
            "description": "Espacio vanguardista con techos de 3.5m, grandes ventanales, zona común abierta y 3 dormitorios espaciosos con mesa de trabajo. Cerca de Metro Pirámides y parque Madrid Río.",
            "city": "Madrid",
            "country": "España",
            "address": "Paseo de la Esperanza, 12, Arganzuela, 28005 Madrid",
            "latitude": 40.4025,
            "longitude": -3.7040,
            "total_rent": 1450.0,
            "ideal_roommates": 3,
            "bedrooms": 3,
            "bathrooms": 2,
            "surface_sqm": 105,
            "property_type": "loft",
            "has_elevator": 1,
            "is_exterior": 1,
            "is_furnished": 1,
            "has_terrace": 1,
            "has_air_con": 1,
            "energy_rating": "A",
            "source_portal": "Pisos.com Open",
            "source_url": "https://www.pisos.com",
            "images": ["static/images/prop-mad-03-1.jpg", "static/images/prop-mad-03-2.jpg", "static/images/prop-mad-03-3.jpg", "static/images/prop-mad-03-4.jpg"],
            "contact_name": "Arganzuela Urban Living",
            "contact_phone": "+34 615 448 990",
            "contact_email": "info@arganzuelaliving.es",
            "contact_whatsapp": "34615448990"
        },
        # Barcelona
        {
            "id": "prop-bcn-01",
            "title": "Modernista al costat de Passeig de Gràcia — 4 habitacions",
            "description": "Pis d'època amb terres hidràulics originals i balcons al carrer. 4 habitacions grans, cuina recent reformada, 2 banys complets i saló menjador espaiós. Ascensor i finca règia cuidada.",
            "city": "Barcelona",
            "country": "España",
            "address": "Carrer d'Aragó, 255, Eixample Dret, 08007 Barcelona",
            "latitude": 41.3912,
            "longitude": 2.1645,
            "total_rent": 1950.0,
            "ideal_roommates": 4,
            "bedrooms": 4,
            "bathrooms": 2,
            "surface_sqm": 135,
            "property_type": "piso",
            "has_elevator": 1,
            "is_exterior": 1,
            "is_furnished": 1,
            "has_terrace": 1,
            "has_air_con": 1,
            "energy_rating": "B",
            "source_portal": "Habitatge Eixample Serveis",
            "source_url": "https://www.habitaclia.com",
            "images": ["static/images/prop-bcn-01-1.jpg", "static/images/prop-bcn-01-2.jpg", "static/images/prop-bcn-01-3.jpg", "static/images/prop-bcn-01-4.jpg"],
            "contact_name": "Habitatge Eixample Serveis Immobiliaris",
            "contact_phone": "+34 932 112 233",
            "contact_email": "info@habitatgeeixample.cat",
            "contact_whatsapp": "34633445566"
        },
        {
            "id": "prop-bcn-02",
            "title": "Àtic amb terrassa a Gràcia — 3 habitacions amb encant",
            "description": "Tranquil i assolellat a la Vila de Gràcia. Terrassa de 25m² per sopars compartits, 3 dormitoris, bany reformat amb dutxa italiana i molta llum natural. Molt a prop de Fontana L3.",
            "city": "Barcelona",
            "country": "España",
            "address": "Carrer del Torrent de l'Olla, 110, Gràcia, 08012 Barcelona",
            "latitude": 41.4021,
            "longitude": 2.1582,
            "total_rent": 1500.0,
            "ideal_roommates": 3,
            "bedrooms": 3,
            "bathrooms": 1,
            "surface_sqm": 90,
            "property_type": "atico",
            "has_elevator": 1,
            "is_exterior": 1,
            "is_furnished": 1,
            "has_terrace": 1,
            "has_air_con": 1,
            "energy_rating": "C",
            "source_portal": "Idealista",
            "source_url": "https://www.idealista.com",
            "images": ["static/images/prop-bcn-02-1.jpg", "static/images/prop-bcn-02-2.jpg", "static/images/prop-bcn-02-3.jpg", "static/images/prop-bcn-02-4.jpg"],
            "contact_name": "Marta Puig (Propietària Particular)",
            "contact_phone": "+34 644 556 677",
            "contact_email": "marta.puig.bcn@gmail.com",
            "contact_whatsapp": "34644556677"
        },
        # Bilbao
        {
            "id": "prop-eusk-01",
            "title": "Etxebizitza zabala Abandon — 4 gela eta 2 bainugela oso",
            "description": "Bilboko erdigunean, tren eta metro geltokietatik 2 minutura. 4 logela handi argitsuak, berogailu zentrala, igogailua eta kanpoaldera begira. Gazte eta langileentzat ezin hobea.",
            "city": "Bilbao",
            "country": "España",
            "address": "Hurtado de Amezaga Kalea, 22, Abando, 48008 Bilbao",
            "latitude": 43.2592,
            "longitude": -2.9338,
            "total_rent": 1400.0,
            "ideal_roommates": 4,
            "bedrooms": 4,
            "bathrooms": 2,
            "surface_sqm": 120,
            "property_type": "piso",
            "has_elevator": 1,
            "is_exterior": 1,
            "is_furnished": 1,
            "has_terrace": 0,
            "has_air_con": 0,
            "energy_rating": "C",
            "source_portal": "Abando Etxebizitza Kudeaketa",
            "source_url": "https://www.idealista.com",
            "images": ["static/images/prop-eusk-01-1.jpg", "static/images/prop-eusk-01-2.jpg", "static/images/prop-eusk-01-3.jpg", "static/images/prop-eusk-01-4.jpg"],
            "contact_name": "Abando Etxebizitza Kudeaketa",
            "contact_phone": "+34 944 123 456",
            "contact_email": "alokairua@abandoetxe.eus",
            "contact_whatsapp": "34655667788"
        },
        # Donostia
        {
            "id": "prop-eusk-02",
            "title": "Pisu argitsua Gros auzoan — Hondartzatik 5 minutura",
            "description": "Donostiako Gros auzoan, Zurriola hondartzatik gertu. 3 gela bikoitz, egongela ederra balkoiarekin, igogailua eta gas bidezko berogailua.",
            "city": "Donostia-San Sebastián",
            "country": "España",
            "address": "Kalea Miracruz, 18, Gros, 20001 Donostia",
            "latitude": 43.3218,
            "longitude": -1.9754,
            "total_rent": 1550.0,
            "ideal_roommates": 3,
            "bedrooms": 3,
            "bathrooms": 2,
            "surface_sqm": 98,
            "property_type": "apartamento",
            "has_elevator": 1,
            "is_exterior": 1,
            "is_furnished": 1,
            "has_terrace": 1,
            "has_air_con": 0,
            "energy_rating": "B",
            "source_portal": "Donosti Coast Real Estate",
            "source_url": "https://www.fotocasa.es",
            "images": ["static/images/prop-eusk-02-1.jpg", "static/images/prop-eusk-02-2.jpg", "static/images/prop-eusk-02-3.jpg", "static/images/prop-eusk-02-4.jpg"],
            "contact_name": "Donosti Coast Real Estate",
            "contact_phone": "+34 943 987 654",
            "contact_email": "contact@donosticoast.com",
            "contact_whatsapp": "34666778899"
        },
        # Paris
        {
            "id": "prop-par-01",
            "title": "Grand appartement haussmannien à Bastille — 4 chambres",
            "description": "Magnifique appartement de 115m² avec parquet point de Hongrie, moulures et cheminées. 4 chambres séparées idéales pour colocation éco-responsable. Cuisine dînatoire équipée, 2 salles de bain.",
            "city": "Paris",
            "country": "France",
            "address": "Rue de la Roquette, 45, 11ème Arrondissement, 75011 Paris",
            "latitude": 48.8558,
            "longitude": 2.3730,
            "total_rent": 2400.0,
            "ideal_roommates": 4,
            "bedrooms": 4,
            "bathrooms": 2,
            "surface_sqm": 115,
            "property_type": "apartamento",
            "has_elevator": 1,
            "is_exterior": 1,
            "is_furnished": 1,
            "has_terrace": 0,
            "has_air_con": 0,
            "energy_rating": "D",
            "source_portal": "Cabinet Immobilier Bastille Paris",
            "source_url": "https://www.seloger.com",
            "images": ["static/images/prop-par-01-1.jpg", "static/images/prop-par-01-2.jpg", "static/images/prop-par-01-3.jpg", "static/images/prop-par-01-4.jpg"],
            "contact_name": "Cabinet Immobilier Bastille Paris",
            "contact_phone": "+33 1 42 68 55 00",
            "contact_email": "location@cabinet-bastille.fr",
            "contact_whatsapp": "33612345678"
        },
        {
            "id": "prop-par-02",
            "title": "Appartement d'architecte au Canal Saint-Martin — 3 chambres",
            "description": "Vue dégagée sur le canal, très calme et lumineux. 3 belles chambres, grand salon convivial, ascenseur, fibre optique et local vélos. Proche métro République.",
            "city": "Paris",
            "country": "France",
            "address": "Quai de Valmy, 92, 10ème Arrondissement, 75010 Paris",
            "latitude": 48.8715,
            "longitude": 2.3654,
            "total_rent": 1980.0,
            "ideal_roommates": 3,
            "bedrooms": 3,
            "bathrooms": 1,
            "surface_sqm": 88,
            "property_type": "apartamento",
            "has_elevator": 1,
            "is_exterior": 1,
            "is_furnished": 1,
            "has_terrace": 1,
            "has_air_con": 0,
            "energy_rating": "C",
            "source_portal": "Jean-Paul Laurent (Propriétaire)",
            "source_url": "https://www.pap.fr",
            "images": ["static/images/prop-par-02-1.jpg", "static/images/prop-par-02-2.jpg", "static/images/prop-par-02-3.jpg", "static/images/prop-par-02-4.jpg"],
            "contact_name": "Jean-Paul Laurent (Propriétaire)",
            "contact_phone": "+33 6 78 90 12 34",
            "contact_email": "jp.laurent.paris@orange.fr",
            "contact_whatsapp": "33678901234"
        },
        # Berlin
        {
            "id": "prop-ber-01",
            "title": "Großzügige Altbau-WG in Kreuzberg — 4 Zimmer mit Balkon",
            "description": "Klassischer Berliner Altbau mit hohen Decken und Dielenboden. 4 separate Zimmer, große Wohnküche, 2 Bäder und Süd-Balkon zum Innenhof. Perfekt für 4 Mitbewohner.",
            "city": "Berlin",
            "country": "Deutschland",
            "address": "Oranienstraße 185, Kreuzberg, 10999 Berlin",
            "latitude": 52.5020,
            "longitude": 13.4190,
            "total_rent": 1840.0,
            "ideal_roommates": 4,
            "bedrooms": 4,
            "bathrooms": 2,
            "surface_sqm": 130,
            "property_type": "piso",
            "has_elevator": 1,
            "is_exterior": 1,
            "is_furnished": 1,
            "has_terrace": 1,
            "has_air_con": 0,
            "energy_rating": "B",
            "source_portal": "Kreuzberg Living Immobilien GmbH",
            "source_url": "https://www.immobilienscout24.de",
            "images": ["static/images/prop-ber-01-1.jpg", "static/images/prop-ber-01-2.jpg", "static/images/prop-ber-01-3.jpg", "static/images/prop-ber-01-4.jpg"],
            "contact_name": "Kreuzberg Living Immobilien GmbH",
            "contact_phone": "+49 30 55443322",
            "contact_email": "vermietung@kreuzberg-living.de",
            "contact_whatsapp": "491512345678"
        },
        {
            "id": "prop-ber-02",
            "title": "Helle 5-Zimmer-Wohnung in Friedrichshain — Boxhagener Platz",
            "description": "5 geräumige Zimmer, renoviertes Badezimmer + Gäste-WC, moderne Einbauküche. Ruhige Seitenstraße, nur 3 Minuten zur U-Bahn Warschauer Straße.",
            "city": "Berlin",
            "country": "Deutschland",
            "address": "Gärtnerstraße 14, Friedrichshain, 10245 Berlin",
            "latitude": 52.5115,
            "longitude": 13.4590,
            "total_rent": 2200.0,
            "ideal_roommates": 5,
            "bedrooms": 5,
            "bathrooms": 2,
            "surface_sqm": 145,
            "property_type": "piso",
            "has_elevator": 1,
            "is_exterior": 1,
            "is_furnished": 1,
            "has_terrace": 0,
            "has_air_con": 0,
            "energy_rating": "C",
            "source_portal": "Friedrichshain Kiez Rentals",
            "source_url": "https://www.wg-gesucht.de",
            "images": ["static/images/prop-ber-02-1.jpg", "static/images/prop-ber-02-2.jpg", "static/images/prop-ber-02-3.jpg", "static/images/prop-ber-02-4.jpg"],
            "contact_name": "Friedrichshain Kiez Rentals",
            "contact_phone": "+49 30 66778899",
            "contact_email": "kiez@fh-rentals.de",
            "contact_whatsapp": "491709876543"
        },
        # Amsterdam
        {
            "id": "prop-ams-01",
            "title": "Spacious Canal Apartment in De Pijp — 3 bedrooms",
            "description": "Beautiful 3-bedroom apartment overlooking the canal. High ceilings, open-concept kitchen, bike storage, elevator, and sunny private balcony. 5 min walk to Sarphatipark.",
            "city": "Amsterdam",
            "country": "Netherlands",
            "address": "Ferdinand Bolstraat 120, De Pijp, 1072 Amsterdam",
            "latitude": 52.3550,
            "longitude": 4.8910,
            "total_rent": 2100.0,
            "ideal_roommates": 3,
            "bedrooms": 3,
            "bathrooms": 2,
            "surface_sqm": 110,
            "property_type": "apartamento",
            "has_elevator": 1,
            "is_exterior": 1,
            "is_furnished": 1,
            "has_terrace": 1,
            "has_air_con": 0,
            "energy_rating": "A",
            "source_portal": "De Pijp Canal Housing B.V.",
            "source_url": "https://www.funda.nl",
            "images": ["static/images/prop-ams-01-1.jpg", "static/images/prop-ams-01-2.jpg", "static/images/prop-ams-01-3.jpg", "static/images/prop-ams-01-4.jpg"],
            "contact_name": "De Pijp Canal Housing B.V.",
            "contact_phone": "+31 20 890 1234",
            "contact_email": "info@depijp-housing.nl",
            "contact_whatsapp": "31612345678"
        },
        # Lisbon
        {
            "id": "prop-lis-01",
            "title": "Apartamento acolhedor com vista Tejo em Alfama — 4 quartos",
            "description": "T4 remodelado com luz fantástica e vista rio. 4 quartos mobilados, 2 casas de banho modernas, cozinha equipada com máquina de lavar louça. Perto de Santa Apolónia.",
            "city": "Lisbon",
            "country": "Portugal",
            "address": "Rua dos Remédios 88, Alfama, 1100-450 Lisboa",
            "latitude": 38.7135,
            "longitude": -9.1270,
            "total_rent": 1600.0,
            "ideal_roommates": 4,
            "bedrooms": 4,
            "bathrooms": 2,
            "surface_sqm": 115,
            "property_type": "apartamento",
            "has_elevator": 0,
            "is_exterior": 1,
            "is_furnished": 1,
            "has_terrace": 1,
            "has_air_con": 1,
            "energy_rating": "B",
            "source_portal": "Alfama Riverfront Properties",
            "source_url": "https://www.idealista.pt",
            "images": ["static/images/prop-lis-01-1.jpg", "static/images/prop-lis-01-2.jpg", "static/images/prop-lis-01-3.jpg", "static/images/prop-lis-01-4.jpg"],
            "contact_name": "Alfama Riverfront Properties",
            "contact_phone": "+351 21 887 6543",
            "contact_email": "arrendamentos@alfamariver.pt",
            "contact_whatsapp": "351912345678"
        },
        # Dublin
        {
            "id": "prop-dub-01",
            "title": "Victorian Townhouse in Portobello — 4 bedrooms for sharing",
            "description": "Substantial 4-bedroom red-brick home in trendy Portobello. Spacious living room, modern kitchen/dining area, garden patio, gas central heating, bus lines directly to city center.",
            "city": "Dublin",
            "country": "Ireland",
            "address": "South Circular Road, Portobello, Dublin 8",
            "latitude": 53.3312,
            "longitude": -6.2715,
            "total_rent": 2400.0,
            "ideal_roommates": 4,
            "bedrooms": 4,
            "bathrooms": 2,
            "surface_sqm": 128,
            "property_type": "casa",
            "has_elevator": 0,
            "is_exterior": 1,
            "is_furnished": 1,
            "has_terrace": 1,
            "has_air_con": 0,
            "energy_rating": "C",
            "source_portal": "Dublin City & Canal Lettings",
            "source_url": "https://www.daft.ie",
            "images": ["static/images/prop-dub-01-1.jpg", "static/images/prop-dub-01-2.jpg", "static/images/prop-dub-01-3.jpg", "static/images/prop-dub-01-4.jpg"],
            "contact_name": "Dublin City & Canal Lettings",
            "contact_phone": "+353 1 497 2233",
            "contact_email": "lettings@dublincitylettings.ie",
            "contact_whatsapp": "353871234567"
        },
        # Rome
        {
            "id": "prop-rom-01",
            "title": "Appartamento spazioso a Trastevere — 4 camere da letto",
            "description": "Nel cuore suggestivo di Trastevere ma in vicolo silenzioso. 4 camere matrimoniali, doppi servizi, cucina abitabile, soffitti con travi in legno, riscaldamento autonomo.",
            "city": "Rome",
            "country": "Italia",
            "address": "Via della Lungaretta, 42, Trastevere, 00153 Roma",
            "latitude": 41.8890,
            "longitude": 12.4730,
            "total_rent": 1750.0,
            "ideal_roommates": 4,
            "bedrooms": 4,
            "bathrooms": 2,
            "surface_sqm": 120,
            "property_type": "piso",
            "has_elevator": 1,
            "is_exterior": 1,
            "is_furnished": 1,
            "has_terrace": 0,
            "has_air_con": 1,
            "energy_rating": "C",
            "source_portal": "Trastevere Dimore Storiche Agenzia",
            "source_url": "https://www.immobiliare.it",
            "images": ["static/images/prop-rom-01-1.jpg", "static/images/prop-rom-01-2.jpg", "static/images/prop-rom-01-3.jpg", "static/images/prop-rom-01-4.jpg"],
            "contact_name": "Trastevere Dimore Storiche Agenzia",
            "contact_phone": "+39 06 6880 1234",
            "contact_email": "locazioni@trasteveredimore.it",
            "contact_whatsapp": "393471234567"
        }
    ]

    for p in properties:
        rent_per_person = round(p["total_rent"] / p["ideal_roommates"], 2)
        db.execute("""
        INSERT INTO properties (
            id, title, description, city, country, address, latitude, longitude,
            total_rent, ideal_roommates, rent_per_person, bedrooms, bathrooms,
            surface_sqm, property_type, has_elevator, is_exterior, is_furnished, has_terrace,
            has_air_con, energy_rating, source_portal, source_url, images,
            contact_name, contact_phone, contact_email, contact_whatsapp,
            status, created_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            p["id"], p["title"], p["description"], p["city"], p["country"], p["address"],
            p["latitude"], p["longitude"], p["total_rent"], p["ideal_roommates"], rent_per_person,
            p["bedrooms"], p["bathrooms"], p["surface_sqm"], p.get("property_type", "piso"),
            p["has_elevator"], p["is_exterior"], p["is_furnished"], p["has_terrace"],
            p["has_air_con"], p["energy_rating"], p["source_portal"], p["source_url"],
            json.dumps(p["images"]),
            p.get("contact_name", "Inmobiliaria / Propietario Directo"),
            p.get("contact_phone", "+34 600 123 456"),
            p.get("contact_email", "contacto@lookingforhome.duckdns.org"),
            p.get("contact_whatsapp", "34600123456"),
            "available", now
        ))

    # Sample Seed Users
    users = [
        ("usr-01", "Elena Gómez", "elena.gomez@example.com", "+34 611 223 344", 24, "Diseñadora UX", 500.0, "Madrid", 4, "Tranquila, ordenada, teletrabajo parcial, me encanta cocinar para el grupo.", ["es", "en"]),
        ("usr-02", "Marc Vila", "marc.vila@example.com", "+34 622 334 455", 27, "Ingeniero de Software", 550.0, "Barcelona", 4, "Amant de l'esport, respectuós amb la convivència i buscant pis a Eixample.", ["ca", "es", "en"]),
        ("usr-03", "Aitor Mendia", "aitor.mendia@example.com", "+34 633 445 566", 26, "Investigador Bioquímico", 450.0, "Bilbao", 4, "Mendizalea, musika zalea eta giro lasaia gustuko duena.", ["eu", "es", "en"]),
        ("usr-04", "Sophie Bernard", "sophie.b@example.com", "+33 6 12 34 56 78", 25, "Architecte Junior", 600.0, "Paris", 4, "Passionnée d'art, vie collective et cuisine conviviale.", ["fr", "en"]),
        ("usr-05", "Lukas Weber", "lukas.weber@example.com", "+49 151 2345678", 28, "Data Analyst", 500.0, "Berlin", 4, "Remote worker, friendly, cycling enthusiast, loves board games.", ["en", "es"])
    ]

    for u in users:
        db.execute("""
        INSERT INTO users (id, name, email, phone, age, occupation, budget_max, preferred_city, preferred_roommates, bio, languages, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (u[0], u[1], u[2], u[3], u[4], u[5], u[6], u[7], u[8], u[9], json.dumps(u[10]), now))

    # Sample Seed Communities
    communities = [
        ("com-01", "Minicomunidad Creativa Malasaña", "prop-mad-01", "Madrid", 4, "Buscamos 1 persona más para cerrar el contrato del ático en Pez. Somos 3 profesionales jóvenes (24-28).", "usr-01", "forming"),
        ("com-02", "Comunitat Sostenible Eixample", "prop-bcn-01", "Barcelona", 4, "Grup de 3 persones buscant 1 company/a per compartir pis modernista. ambient tranquil i respectuós.", "usr-02", "forming"),
        ("com-03", "Euskal Taldea Bilbo", "prop-eusk-01", "Bilbao", 4, "3 lagun gara Abandoko etxea hartzeko prest, laugarren baten bila gabiltza gastuak banatzeko.", "usr-03", "forming"),
        ("com-04", "Coloc Bastille Eco-Living", "prop-par-01", "Paris", 4, "Nous sommes 3 colocataires dans l'appartement haussmannien. Nous cherchons le 4ème membre.", "usr-04", "forming")
    ]

    for c in communities:
        db.execute("""
        INSERT INTO communities (id, name, property_id, city, max_members, description, created_by_user_id, status, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (c[0], c[1], c[2], c[3], c[4], c[5], c[6], c[7], now))

    # Link members to communities
    db.execute("INSERT INTO community_members (id, community_id, user_id, role, rent_share, fee_paid, joined_at) VALUES (?, ?, ?, ?, ?, ?, ?)",
               ("cm-01", "com-01", "usr-01", "creator", 450.0, 1, now))
    db.execute("INSERT INTO community_members (id, community_id, user_id, role, rent_share, fee_paid, joined_at) VALUES (?, ?, ?, ?, ?, ?, ?)",
               ("cm-02", "com-02", "usr-02", "creator", 487.5, 1, now))
    db.execute("INSERT INTO community_members (id, community_id, user_id, role, rent_share, fee_paid, joined_at) VALUES (?, ?, ?, ?, ?, ?, ?)",
               ("cm-03", "com-03", "usr-03", "creator", 350.0, 1, now))
    db.execute("INSERT INTO community_members (id, community_id, user_id, role, rent_share, fee_paid, joined_at) VALUES (?, ?, ?, ?, ?, ?, ?)",
               ("cm-04", "com-04", "usr-04", "creator", 600.0, 1, now))


def _update_seed_contact_info(db: DBContext):
    # Ensure known properties have their realistic contact info, local image sets, types, and official deep listing URLs
    contact_map = {
        "prop-mad-01": ("Carlos Mendoza (Propietario Directo)", "+34 611 223 344", "carlos.mendoza.mad@gmail.com", "34611223344", "atico", "https://www.idealista.com/inmueble/98412039/"),
        "prop-mad-02": ("Inmobiliaria Chamberí Siglo XXI", "+34 914 556 789", "alquileres@chamberisigloxxi.es", "34622334455", "piso", "https://www.fotocasa.es/es/alquiler/vivienda/madrid-capital/chamberi/178942319/d"),
        "prop-mad-03": ("Arganzuela Urban Living", "+34 615 448 990", "info@arganzuelaliving.es", "34615448990", "loft", "https://www.pisos.com/alquiler/piso-madrid_arganzuela-289182390_100200/"),
        "prop-bcn-01": ("Habitatge Eixample Serveis Immobiliaris", "+34 932 112 233", "info@habitatgeeixample.cat", "34633445566", "piso", "https://www.habitaclia.com/alquiler-piso-eixample_barcelona-i4920003928172.htm"),
        "prop-bcn-02": ("Marta Puig (Propietària Particular)", "+34 644 556 677", "marta.puig.bcn@gmail.com", "34644556677", "atico", "https://www.idealista.com/inmueble/99824102/"),
        "prop-eusk-01": ("Abando Etxebizitza Kudeaketa", "+34 944 123 456", "alokairua@abandoetxe.eus", "34655667788", "piso", "https://www.idealista.com/inmueble/101938472/"),
        "prop-eusk-02": ("Donosti Coast Real Estate", "+34 943 987 654", "contact@donosticoast.com", "34666778899", "apartamento", "https://www.fotocasa.es/es/alquiler/vivienda/donostia-san-sebastian/gros/182940192/d"),
        "prop-par-01": ("Cabinet Immobilier Bastille Paris", "+33 1 42 68 55 00", "location@cabinet-bastille.fr", "33612345678", "apartamento", "https://www.seloger.com/annonces/locations/appartement/paris-11eme/20491823.htm"),
        "prop-par-02": ("Jean-Paul Laurent (Propriétaire)", "+33 6 78 90 12 34", "jp.laurent.paris@orange.fr", "33678901234", "apartamento", "https://www.pap.fr/annonces/appartement-paris-5e-r449201928"),
        "prop-ber-01": ("Kreuzberg Living Immobilien GmbH", "+49 30 55443322", "vermietung@kreuzberg-living.de", "491512345678", "piso", "https://www.immobilienscout24.de/expose/149201982"),
        "prop-ber-02": ("Friedrichshain Kiez Rentals", "+49 30 66778899", "kiez@fh-rentals.de", "491709876543", "piso", "https://www.wg-gesucht.de/wg-zimmer-in-Berlin-Friedrichshain.9841029.html"),
        "prop-ams-01": ("De Pijp Canal Housing B.V.", "+31 20 890 1234", "info@depijp-housing.nl", "31612345678", "apartamento", "https://www.funda.nl/huur/amsterdam/appartement-42918274/"),
        "prop-lis-01": ("Alfama Riverfront Properties", "+351 21 887 6543", "arrendamentos@alfamariver.pt", "351912345678", "apartamento", "https://www.idealista.pt/imovel/32948192/"),
        "prop-dub-01": ("Dublin City & Canal Lettings", "+353 1 497 2233", "lettings@dublincitylettings.ie", "353871234567", "casa", "https://www.daft.ie/for-rent/apartment-grand-canal-dock-dublin/5928102"),
        "prop-rom-01": ("Trastevere Dimore Storiche Agenzia", "+39 06 6880 1234", "locazioni@trasteveredimore.it", "393471234567", "piso", "https://www.immobiliare.it/annunci/10928471/")
    }

    for pid, (c_name, c_phone, c_email, c_wa, p_type, s_url) in contact_map.items():
        imgs = json.dumps([f"static/images/{pid}-{i}.jpg" for i in range(1, 5)])
        db.execute("""
        UPDATE properties
        SET contact_name = ?, contact_phone = ?, contact_email = ?, contact_whatsapp = ?, property_type = ?, images = ?, source_url = ?
        WHERE id = ?
        """, (c_name, c_phone, c_email, c_wa, p_type, imgs, s_url, pid))


# ── Query Helper Functions ───────────────────────────────────────────────────

def get_properties(
    city: Optional[str] = None,
    country: Optional[str] = None,
    property_type: Optional[str] = None,
    min_bedrooms: Optional[int] = None,
    min_bathrooms: Optional[int] = None,
    min_surface_sqm: Optional[int] = None,
    max_surface_sqm: Optional[int] = None,
    has_elevator: Optional[bool] = None,
    is_exterior: Optional[bool] = None,
    max_rent_per_person: Optional[float] = None,
    max_total_rent: Optional[float] = None
) -> List[Dict[str, Any]]:
    with DBContext() as db:
        query = "SELECT * FROM properties WHERE 1=1"
        params = []

        if city and city != "all":
            query += " AND LOWER(city) = LOWER(?)"
            params.append(city)
        if country and country != "all":
            query += " AND LOWER(country) = LOWER(?)"
            params.append(country)
        if property_type and property_type != "all":
            query += " AND LOWER(property_type) = LOWER(?)"
            params.append(property_type)
        if min_bedrooms:
            query += " AND bedrooms >= ?"
            params.append(min_bedrooms)
        if min_bathrooms:
            query += " AND bathrooms >= ?"
            params.append(min_bathrooms)
        if min_surface_sqm:
            query += " AND surface_sqm >= ?"
            params.append(min_surface_sqm)
        if max_surface_sqm:
            query += " AND surface_sqm <= ?"
            params.append(max_surface_sqm)
        if has_elevator is not None:
            query += " AND has_elevator = ?"
            params.append(1 if has_elevator else 0)
        if is_exterior is not None:
            query += " AND is_exterior = ?"
            params.append(1 if is_exterior else 0)
        if max_rent_per_person:
            query += " AND rent_per_person <= ?"
            params.append(max_rent_per_person)
        if max_total_rent:
            query += " AND total_rent <= ?"
            params.append(max_total_rent)

        query += " ORDER BY created_at DESC"
        db.execute(query, tuple(params) if params else None)
        rows = db.fetchall()

    result = []
    for r in rows:
        d = dict(r)
        d["images"] = json.loads(d["images"]) if d.get("images") else []
        d["has_elevator"] = bool(d.get("has_elevator", 1))
        d["is_exterior"] = bool(d.get("is_exterior", 1))
        d["is_furnished"] = bool(d.get("is_furnished", 1))
        d["has_terrace"] = bool(d.get("has_terrace", 0))
        d["has_air_con"] = bool(d.get("has_air_con", 0))
        result.append(d)
    return result


def get_property(property_id: str) -> Optional[Dict[str, Any]]:
    with DBContext() as db:
        db.execute("SELECT * FROM properties WHERE id = ?", (property_id,))
        row = db.fetchone()

    if not row:
        return None
    d = dict(row)
    d["images"] = json.loads(d["images"]) if d.get("images") else []
    d["has_elevator"] = bool(d.get("has_elevator", 1))
    d["is_exterior"] = bool(d.get("is_exterior", 1))
    d["is_furnished"] = bool(d.get("is_furnished", 1))
    d["has_terrace"] = bool(d.get("has_terrace", 0))
    d["has_air_con"] = bool(d.get("has_air_con", 0))
    return d


def create_property(prop_dict: Dict[str, Any]) -> str:
    prop_id = str(uuid.uuid4())[:8]
    now = datetime.now(timezone.utc).isoformat()
    rent_pp = round(prop_dict["total_rent"] / prop_dict["ideal_roommates"], 2)

    with DBContext() as db:
        db.execute("""
        INSERT INTO properties (
            id, title, description, city, country, address, latitude, longitude,
            total_rent, ideal_roommates, rent_per_person, bedrooms, bathrooms,
            surface_sqm, property_type, has_elevator, is_exterior, is_furnished, has_terrace,
            has_air_con, energy_rating, source_portal, source_url, images,
            contact_name, contact_phone, contact_email, contact_whatsapp,
            status, created_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            prop_id, prop_dict["title"], prop_dict.get("description", ""),
            prop_dict["city"], prop_dict["country"], prop_dict["address"],
            prop_dict["latitude"], prop_dict["longitude"], prop_dict["total_rent"],
            prop_dict["ideal_roommates"], rent_pp, prop_dict["bedrooms"],
            prop_dict["bathrooms"], prop_dict["surface_sqm"],
            prop_dict.get("property_type", "piso"),
            1 if prop_dict.get("has_elevator", True) else 0,
            1 if prop_dict.get("is_exterior", True) else 0,
            1 if prop_dict.get("is_furnished", True) else 0,
            1 if prop_dict.get("has_terrace", False) else 0,
            1 if prop_dict.get("has_air_con", False) else 0,
            prop_dict.get("energy_rating", "B"),
            prop_dict.get("source_portal", "Direct User Submission"),
            prop_dict.get("source_url", ""),
            json.dumps(prop_dict.get("images", [])),
            prop_dict.get("contact_name", "Inmobiliaria / Propietario Directo"),
            prop_dict.get("contact_phone", "+34 600 123 456"),
            prop_dict.get("contact_email", "contacto@lookingforhome.duckdns.org"),
            prop_dict.get("contact_whatsapp", "34600123456"),
            "available", now
        ))
    return prop_id


def get_communities(city: Optional[str] = None) -> List[Dict[str, Any]]:
    with DBContext() as db:
        q = "SELECT c.*, p.title as prop_title, p.address as prop_address, p.total_rent, p.rent_per_person FROM communities c LEFT JOIN properties p ON c.property_id = p.id WHERE 1=1"
        params = []
        if city and city != "all":
            q += " AND LOWER(c.city) = LOWER(?)"
            params.append(city)
        q += " ORDER BY c.created_at DESC"

        db.execute(q, tuple(params) if params else None)
        rows = db.fetchall()

        result = []
        for r in rows:
            c_dict = dict(r)
            db.execute("""
            SELECT u.id, u.name, u.email, u.phone, u.age, u.occupation, cm.role, cm.fee_paid
            FROM community_members cm
            JOIN users u ON cm.user_id = u.id
            WHERE cm.community_id = ?
            """, (c_dict["id"],))
            members = db.fetchall()
            c_dict["members"] = members
            c_dict["current_members_count"] = len(members)
            result.append(c_dict)

    return result


def create_community(data: Dict[str, Any]) -> str:
    c_id = str(uuid.uuid4())[:8]
    now = datetime.now(timezone.utc).isoformat()

    with DBContext() as db:
        db.execute("""
        INSERT INTO communities (id, name, property_id, city, max_members, description, created_by_user_id, status, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            c_id, data["name"], data.get("property_id"), data["city"],
            data.get("max_members", 4), data.get("description", ""),
            data.get("created_by_user_id"), "forming", now
        ))

        if data.get("created_by_user_id"):
            db.execute("""
            INSERT INTO community_members (id, community_id, user_id, role, fee_paid, joined_at)
            VALUES (?, ?, ?, 'creator', 1, ?)
            """, (str(uuid.uuid4())[:8], c_id, data["created_by_user_id"], now))

    return c_id


def join_community(community_id: str, user_id: str, fee_paid: bool = False) -> bool:
    now = datetime.now(timezone.utc).isoformat()

    with DBContext() as db:
        db.execute("SELECT max_members FROM communities WHERE id = ?", (community_id,))
        com = db.fetchone()
        if not com:
            return False

        db.execute("SELECT COUNT(*) FROM community_members WHERE community_id = ?", (community_id,))
        count = db.fetchval()
        if count >= com["max_members"]:
            return False

        db.execute("""
        INSERT INTO community_members (id, community_id, user_id, role, fee_paid, joined_at)
        VALUES (?, ?, ?, 'member', ?, ?)
        """, (str(uuid.uuid4())[:8], community_id, user_id, 1 if fee_paid else 0, now))

    return True


def create_user(u: Dict[str, Any]) -> str:
    uid = str(uuid.uuid4())[:8]
    now = datetime.now(timezone.utc).isoformat()

    with DBContext() as db:
        db.execute("""
        INSERT INTO users (id, name, email, phone, age, occupation, budget_max, preferred_city, preferred_roommates, bio, languages, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            uid, u["name"], u["email"], u["phone"], u.get("age", 25),
            u.get("occupation", "Estudiante / Trabajador"), u.get("budget_max", 500.0),
            u.get("preferred_city", "Madrid"), u.get("preferred_roommates", 4),
            u.get("bio", ""), json.dumps(u.get("languages", ["es", "en"])), now
        ))

    return uid


def get_users() -> List[Dict[str, Any]]:
    with DBContext() as db:
        db.execute("SELECT * FROM users ORDER BY created_at DESC")
        rows = db.fetchall()

    res = []
    for r in rows:
        d = dict(r)
        d["languages"] = json.loads(d["languages"]) if d.get("languages") else []
        res.append(d)
    return res


def save_inquiry(inquiry_dict: Dict[str, Any]) -> str:
    iq_id = str(uuid.uuid4())[:8]
    now = datetime.now(timezone.utc).isoformat()

    with DBContext() as db:
        db.execute("""
        INSERT INTO inquiries (id, property_id, user_name, user_email, user_phone, message, community_id, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            iq_id, inquiry_dict["property_id"], inquiry_dict["name"],
            inquiry_dict["email"], inquiry_dict["phone"], inquiry_dict["message"],
            inquiry_dict.get("community_id"), now
        ))

    return iq_id


# ── Access Logs & Visitor Analytics ──────────────────────────────────────────

def record_access_log(
    ip: str,
    country: str = "Desconocido",
    country_code: str = "UN",
    region: str = "",
    city: str = "Desconocido",
    latitude: float = 0.0,
    longitude: float = 0.0,
    path: str = "/",
    method: str = "GET",
    status_code: int = 200,
    user_agent: str = "",
    device_type: str = "Desktop",
    referrer: str = ""
) -> str:
    log_id = f"log-{uuid.uuid4().hex[:12]}"
    now = datetime.now(timezone.utc).isoformat()

    with DBContext() as db:
        db.execute("""
        INSERT INTO access_logs (
            id, ip, country, country_code, region, city, latitude, longitude,
            path, method, status_code, user_agent, device_type, referrer, created_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            log_id, ip, country, country_code, region, city, latitude, longitude,
            path, method, status_code, (user_agent or "")[:500],
            device_type, (referrer or "")[:500], now
        ))

    return log_id


def get_access_logs(limit: int = 100, country: Optional[str] = None, search: Optional[str] = None) -> List[Dict[str, Any]]:
    with DBContext() as db:
        query = "SELECT * FROM access_logs WHERE 1=1"
        params = []

        if country:
            query += " AND (country = ? OR country_code = ?)"
            params.extend([country, country.upper()])

        if search:
            query += " AND (ip LIKE ? OR city LIKE ? OR country LIKE ? OR path LIKE ?)"
            s = f"%{search}%"
            params.extend([s, s, s, s])

        query += " ORDER BY created_at DESC LIMIT ?"
        params.append(min(limit, 500))

        db.execute(query, tuple(params))
        rows = db.fetchall()

    return [dict(r) for r in rows]


def get_access_stats() -> Dict[str, Any]:
    with DBContext() as db:
        # Total visits
        db.execute("SELECT COUNT(*) FROM access_logs")
        total_visits = db.fetchval() or 0

        # Unique IPs
        db.execute("SELECT COUNT(DISTINCT ip) FROM access_logs")
        unique_ips = db.fetchval() or 0

        # Today's visits (UTC prefix match)
        today_prefix = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        db.execute("SELECT COUNT(*) FROM access_logs WHERE created_at LIKE ?", (f"{today_prefix}%",))
        today_visits = db.fetchval() or 0

        # Country breakdown
        db.execute("""
        SELECT country, country_code, COUNT(*) as visit_count, COUNT(DISTINCT ip) as unique_visitors
        FROM access_logs
        GROUP BY country, country_code
        ORDER BY visit_count DESC
        LIMIT 10
        """)
        top_countries = [dict(r) for r in db.fetchall()]

        # Device breakdown
        db.execute("""
        SELECT device_type, COUNT(*) as count
        FROM access_logs
        GROUP BY device_type
        ORDER BY count DESC
        """)
        device_breakdown = [dict(r) for r in db.fetchall()]

        # Geographic coordinates grouped by location for Leaflet map markers
        db.execute("""
        SELECT 
            city, country, country_code, latitude, longitude,
            COUNT(*) as visit_count,
            COUNT(DISTINCT ip) as unique_ips,
            MAX(created_at) as last_seen
        FROM access_logs
        WHERE latitude != 0.0 AND longitude != 0.0
        GROUP BY city, country, country_code, latitude, longitude
        ORDER BY visit_count DESC
        LIMIT 100
        """)
        geo_locations = [dict(r) for r in db.fetchall()]

    return {
        "total_visits": total_visits,
        "unique_ips": unique_ips,
        "today_visits": today_visits,
        "top_countries": top_countries,
        "device_breakdown": device_breakdown,
        "geo_locations": geo_locations
    }


def clear_access_logs() -> bool:
    with DBContext() as db:
        db.execute("DELETE FROM access_logs")
    return True


def _seed_access_logs(db: DBContext):
    """Populates realistic initial visitor logs across European & global locations."""
    now = datetime.now(timezone.utc)
    
    seed_visitors = [
        # Madrid
        ("83.54.120.45", "España", "ES", "Madrid", "Madrid", 40.4168, -3.7038, "/", "Desktop", "Chrome on Windows"),
        ("88.12.94.18", "España", "ES", "Madrid", "Madrid", 40.4238, -3.7065, "/api/v1/properties", "Mobile", "Safari on iPhone"),
        ("212.128.4.10", "España", "ES", "Madrid", "Alcalá de Henares", 40.4819, -3.3643, "/lookingforhome/", "Desktop", "Firefox on macOS"),
        # Barcelona & Catalunya
        ("81.184.22.91", "España", "ES", "Catalunya", "Barcelona", 41.3851, 2.1734, "/", "Desktop", "Chrome on macOS"),
        ("84.120.15.63", "España", "ES", "Catalunya", "Barcelona", 41.3980, 2.1950, "/lookingforhome/", "Mobile", "Chrome on Android"),
        ("188.78.204.12", "España", "ES", "Catalunya", "Girona", 41.9794, 2.8214, "/", "Desktop", "Safari on macOS"),
        # Valencia & Alicante
        ("80.25.170.82", "España", "ES", "Comunidad Valenciana", "Valencia", 39.4699, -0.3763, "/", "Mobile", "Chrome on Android"),
        ("88.24.110.15", "España", "ES", "Comunidad Valenciana", "Alicante", 38.3452, -0.4810, "/api/v1/properties", "Desktop", "Edge on Windows"),
        # Andalucía (Sevilla, Málaga, Granada)
        ("90.168.42.19", "España", "ES", "Andalucía", "Sevilla", 37.3891, -5.9845, "/", "Desktop", "Chrome on Windows"),
        ("81.33.201.74", "España", "ES", "Andalucía", "Málaga", 36.7213, -4.4214, "/lookingforhome/", "Mobile", "Safari on iPhone"),
        ("85.137.90.11", "España", "ES", "Andalucía", "Granada", 37.1773, -3.5986, "/", "Desktop", "Chrome on Linux"),
        # Euskadi (Bilbao, San Sebastián)
        ("85.84.14.22", "España", "ES", "País Vasco", "Bilbao", 43.2630, -2.9350, "/", "Desktop", "Firefox on Linux"),
        ("83.213.88.51", "España", "ES", "País Vasco", "Donostia-San Sebastián", 43.3183, -1.9812, "/lookingforhome/", "Desktop", "Safari on macOS"),
        # Zaragoza & Salamanca
        ("88.7.192.40", "España", "ES", "Aragón", "Zaragoza", 41.6488, -0.8891, "/", "Mobile", "Chrome on Android"),
        ("84.126.33.10", "España", "ES", "Castilla y León", "Salamanca", 40.9701, -5.6635, "/", "Desktop", "Chrome on Windows"),
        # France (Paris, Lyon)
        ("92.184.112.44", "Francia", "FR", "Île-de-France", "Paris", 48.8566, 2.3522, "/", "Desktop", "Chrome on macOS"),
        ("90.84.210.19", "Francia", "FR", "Auvergne-Rhône-Alpes", "Lyon", 45.7640, 4.8357, "/lookingforhome/", "Mobile", "Safari on iPhone"),
        # Germany (Berlin, Munich, Frankfurt)
        ("178.62.204.88", "Alemania", "DE", "Berlin", "Berlin", 52.5200, 13.4050, "/", "Desktop", "Firefox on Windows"),
        ("91.65.180.22", "Alemania", "DE", "Bavaria", "Múnich", 48.1351, 11.5820, "/lookingforhome/", "Desktop", "Chrome on Windows"),
        # Netherlands (Amsterdam, Rotterdam)
        ("145.131.40.12", "Países Bajos", "NL", "North Holland", "Ámsterdam", 52.3676, 4.9041, "/", "Desktop", "Chrome on macOS"),
        # Portugal (Lisboa, Porto)
        ("194.65.230.14", "Portugal", "PT", "Lisboa", "Lisboa", 38.7223, -9.1393, "/", "Mobile", "Chrome on Android"),
        ("188.82.10.95", "Portugal", "PT", "Porto", "Porto", 41.1579, -8.6291, "/lookingforhome/", "Desktop", "Safari on macOS"),
        # Italy (Roma, Milano)
        ("151.48.90.31", "Italia", "IT", "Lazio", "Roma", 41.9028, 12.4964, "/", "Desktop", "Edge on Windows"),
        ("93.41.120.65", "Italia", "IT", "Lombardia", "Milán", 45.4642, 9.1900, "/lookingforhome/", "Mobile", "Safari on iPhone"),
        # Ireland (Dublin)
        ("185.120.88.19", "Irlanda", "IE", "Leinster", "Dublín", 53.3498, -6.2603, "/", "Desktop", "Chrome on macOS"),
        # United Kingdom (London)
        ("86.154.210.42", "Reino Unido", "GB", "Greater London", "Londres", 51.5074, -0.1278, "/", "Desktop", "Safari on macOS"),
        # United States & Latin America
        ("104.28.34.164", "Estados Unidos", "US", "California", "San Francisco", 37.7749, -122.4194, "/", "Desktop", "Chrome on macOS"),
        ("186.108.92.15", "Argentina", "AR", "Buenos Aires", "Buenos Aires", -34.6037, -58.3816, "/lookingforhome/", "Mobile", "Chrome on Android"),
        ("189.200.45.18", "México", "MX", "Ciudad de México", "Ciudad de México", 19.4326, -99.1332, "/", "Mobile", "Safari on iPhone"),
        ("181.140.22.80", "Colombia", "CO", "Bogotá", "Bogotá", 4.7110, -74.0721, "/", "Desktop", "Chrome on Windows")
    ]

    from datetime import timedelta
    for i, item in enumerate(seed_visitors):
        ip, country, ccode, region, city, lat, lng, path, dev, ua = item
        # Distribute timestamps over last 48 hours
        t_delta = timedelta(hours=(len(seed_visitors) - i) * 1.5, minutes=(i * 17) % 60)
        t_str = (now - t_delta).isoformat()
        log_id = f"seed-log-{i+1:03d}"

        db.execute("""
        INSERT INTO access_logs (
            id, ip, country, country_code, region, city, latitude, longitude,
            path, method, status_code, user_agent, device_type, referrer, created_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            log_id, ip, country, ccode, region, city, lat, lng,
            path, "GET", 200, ua, dev, "https://lookingforhome.duckdns.org", t_str
        ))

