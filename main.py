from fastapi import FastAPI
from pydantic import BaseModel
from products import products

app = FastAPI()


class Product(BaseModel):
    name: str
    quantity: int
    price: float
    description: str | None = None

@app.get("/")
async def listProducts():
    status = ""
    if len(products) >= 1:
        status = 200
    else:
        status = 204
    return {
        "status": status,
        "message": products
    }

@app.post("/product/")
async def createProduct(product: Product):
    products.append({
        "name": product.name,
        "quantity": product.quantity,
        "price": product.price,
        "description": product.description
    })

    return {
        "status": "200",
        "mensagem": f"{product.name} cadastrado com sucesso!"
    }

@app.put("/product/{name}")
async def updateProduct(name: str, product: Product):
    status = 204
    msg = ""
    for p in products:
        if p["name"] == name:
            p["name"] = product.name
            p["quantity"] = product.quantity
            p["price"] = product.price
            p["description"] = product.description
            msg = "alteracao feita com sucesso"
            status = 200

            break

    return {
        "status": status,
        "messagem": msg
    }

@app.delete("/product/{name}")
async def deleteProdutc(name: str):
    msg = ""
    status = 204
    for i in range(0, len(products)):
        if products[i]["name"] == name:
            products.pop(i)
            status = 200
            msg = "produto excluido"
            break

    return {
        "status": status,
        "msg": msg
    }
