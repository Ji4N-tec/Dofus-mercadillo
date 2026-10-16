import json
import requests

URL = "https://api.dofusdb.fr"

# 1) Pedimos UNA receta de alquimista (el oficio suele tener el id 26)
r = requests.get(
    f"{URL}/recipes",
    params={"$limit": 1, "jobId": 26, "lang": "es"},
    timeout=30,
)
print("Código de respuesta:", r.status_code)
datos = r.json()

# Guardamos la respuesta completa en un archivo para poder mirarla con calma
with open("muestra_receta.json", "w", encoding="utf-8") as f:
    json.dump(datos, f, ensure_ascii=False, indent=2)

print("Total de recetas de ese oficio:", datos.get("total"))
print("Campos de la primera receta:")
if datos.get("data"):
    for campo in datos["data"][0].keys():
        print(" -", campo)
else:
    print("No llegó ninguna receta. Mira muestra_receta.json")