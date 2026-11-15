from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List, Dict, Any
from datetime import datetime


class PropertyBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=150)
    description: str
    city: str
    country: str
    address: str
    latitude: float
    longitude: float
    total_rent: float = Field(..., gt=0, description="Monthly total rent in EUR")
    ideal_roommates: int = Field(4, ge=2, le=6, description="Recommended community size (3-5 people)")
    bedrooms: int = Field(..., ge=1, le=10)
    bathrooms: int = Field(..., ge=1, le=6)
    surface_sqm: int = Field(..., ge=20, le=500)
    has_elevator: bool = True
    is_exterior: bool = True
    is_furnished: bool = True
    has_terrace: bool = False
    has_air_con: bool = False
    energy_rating: str = Field("B", max_length=2)
    source_portal: str = Field("Open Portal", max_length=50)
    source_url: Optional[str] = None
    property_type: str = Field("piso", description="piso, apartamento, atico, casa, loft")
    images: List[str] = Field(default_factory=list)
    contact_name: Optional[str] = Field("Inmobiliaria / Propietario Directo", max_length=120)
    contact_phone: Optional[str] = Field("+34 600 123 456", max_length=50)
    contact_email: Optional[str] = Field("contacto@lookingforhome.duckdns.org", max_length=120)
    contact_whatsapp: Optional[str] = Field("34600123456", max_length=50)


class PropertyCreate(PropertyBase):
    pass


class PropertyResponse(PropertyBase):
    id: str
    rent_per_person: float
    status: str
    created_at: str


class UserCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: str = Field(..., min_length=5, max_length=120)
    phone: str = Field(..., min_length=6, max_length=30)
    age: int = Field(25, ge=18, le=99)
    occupation: str = Field("Estudiante / Trabajador", max_length=100)
    budget_max: float = Field(500.0, gt=50)
    preferred_city: str = Field("Madrid", max_length=60)
    preferred_roommates: int = Field(4, ge=2, le=5)
    bio: Optional[str] = Field(None, max_length=500)
    languages: List[str] = Field(default_factory=lambda: ["es", "en"])


class UserResponse(UserCreate):
    id: str
    created_at: str


class CommunityCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    property_id: Optional[str] = None
    city: str
    max_members: int = Field(4, ge=2, le=6)
    description: Optional[str] = None
    created_by_user_id: Optional[str] = None


class CommunityMemberAdd(BaseModel):
    user_id: str
    role: str = Field("member", max_length=30)
    rent_share: Optional[float] = None
    fee_paid: bool = False


class CommunityResponse(BaseModel):
    id: str
    name: str
    property_id: Optional[str] = None
    city: str
    max_members: int
    current_members_count: int
    description: Optional[str] = None
    status: str
    created_at: str
    property: Optional[Dict[str, Any]] = None
    members: List[Dict[str, Any]] = []


class InquiryCreate(BaseModel):
    property_id: str
    name: str
    email: str
    phone: str
    message: str
    community_id: Optional[str] = None


class PortalImportRequest(BaseModel):
    portal_name: str
    portal_url: str
    city: str
    country: str
    target_rent: Optional[float] = None
    bedrooms: Optional[int] = None
