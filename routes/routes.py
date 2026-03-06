from fastapi import APIRouter, Depends
from schemas.lead import LeadRequest
from services.utils import save_lead, read_leads
from datetime import datetime
import json

router = APIRouter()


@router.get("/")
def welcome():
    return {"message": "Bienvenido a mi API de leads!"}

@router.post("/leads")
def addLeads(payload: LeadRequest):
    try: 
        data = payload.dict()
        create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        save_lead(data)
        return {
            "status": "ok",
            "description": "✅Lead guardado correctamente",
            "create_at": create_at,
            "data": data
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"🚨Ocurrio un error al intentar registar Lead {str(e)}"
        }

@router.get("/leads")
def getLeads():
    try:
        leads = read_leads()
        return {
            "status": "ok",
            "description": "✅Leads obtenidos correctamente",
            "data": leads
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"🚨Ocurrio un error al intentar obtener los Leads {str(e)}"
        }