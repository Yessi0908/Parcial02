def borrar_producto_por_sku(sku):
    # Buscar producto por SKU y borrarlo si existe
    r = client.get("/apiv1/productos/")
    if r.status_code == 200:
        for prod in r.json():
            if prod["sku"] == sku:
                client.delete(f"/apiv1/productos/{prod['id']}")


import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Datos de prueba
producto_1 = {
    "nombre": "PanFrancés",
    "sku": "PAN-0001",
    "categoria": "Pan",
    "precio_unitario": 1.25,
    "stock": 120
}

producto_2 = {
    "nombre": "Croissant",
    "sku": "PAS-0101",
    "categoria": "Pastelería",
    "precio_unitario": 2.75,
    "stock": 60
}


def test_crear_producto():
    borrar_producto_por_sku(producto_1["sku"])
    r = client.post("/apiv1/productos/", json=producto_1)
    assert r.status_code == 201
    data = r.json()
    assert data["sku"] == producto_1["sku"]
    # Cleanup
    client.delete(f"/apiv1/productos/{data['id']}")

def test_crear_producto_sku_duplicado():
    borrar_producto_por_sku(producto_1["sku"])
    r1 = client.post("/apiv1/productos/", json=producto_1)
    assert r1.status_code == 201
    r2 = client.post("/apiv1/productos/", json=producto_1)
    assert r2.status_code == 400
    # Cleanup
    data = r1.json()
    client.delete(f"/apiv1/productos/{data['id']}")

def test_listar_productos():
    borrar_producto_por_sku(producto_2["sku"])
    r1 = client.post("/apiv1/productos/", json=producto_2)
    assert r1.status_code == 201
    r = client.get("/apiv1/productos/")
    assert r.status_code == 200
    assert isinstance(r.json(), list)
    # Cleanup
    data = r1.json()
    client.delete(f"/apiv1/productos/{data['id']}")

def test_obtener_producto():
    borrar_producto_por_sku(producto_1["sku"])
    r1 = client.post("/apiv1/productos/", json=producto_1)
    assert r1.status_code == 201
    data = r1.json()
    r = client.get(f"/apiv1/productos/{data['id']}")
    assert r.status_code == 200
    assert r.json()["sku"] == producto_1["sku"]
    # Cleanup
    client.delete(f"/apiv1/productos/{data['id']}")

def test_actualizar_producto():
    borrar_producto_por_sku(producto_1["sku"])
    r1 = client.post("/apiv1/productos/", json=producto_1)
    assert r1.status_code == 201
    data = r1.json()
    # Enviar todos los campos válidos para update
    update_data = {
        "nombre": data["nombre"],
        "categoria": data["categoria"],
        "precio_unitario": 1.5,
        "stock": data["stock"],
        "disponible": data.get("disponible", True)
    }
    r = client.put(f"/apiv1/productos/{data['id']}", json=update_data)
    assert r.status_code == 200
    assert r.json()["precio_unitario"] == 1.5
    # Cleanup
    client.delete(f"/apiv1/productos/{data['id']}")

def test_eliminar_producto():
    borrar_producto_por_sku(producto_1["sku"])
    r1 = client.post("/apiv1/productos/", json=producto_1)
    assert r1.status_code == 201
    data = r1.json()
    r = client.delete(f"/apiv1/productos/{data['id']}")
    assert r.status_code == 200
    # Ya no existe
    r2 = client.get(f"/apiv1/productos/{data['id']}")
    assert r2.status_code == 404
