from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

def test_mongo(request):
  
    try:
    
        from CoolSense.settings import mongo_db
        if mongo_db:
            result = mongo_db.logs.insert_one({"msg": "Olá Mongo!"})
            return JsonResponse({"id": str(result.inserted_id)})
        return JsonResponse({"error": "MongoDB not connected"}, status=503)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=503)

def api_root(request):
    """Root endpoint that shows API information"""
    return JsonResponse({
        "message": "CoolSense API",
        "version": "1.0.0",
        "endpoints": {
            "sensors": "/api/sensors/",
            "admin": "/admin/",
        },
        "documentation": "Access /api/sensors/ for the sensors API endpoint"
    })

