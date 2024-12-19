from docxtpl import DocxTemplate
import os
""" import os
os.makedirs("app/outputs", exist_ok=True) """


def convertir(nombre_doc,plantilla, contexto,BASE_DIR):

    # Construir rutas absolutas usando el directorio base
    ruta_plantilla = os.path.join(BASE_DIR,"inputs",  f"{plantilla}.docx")
    ruta_salida = os.path.join(BASE_DIR,"outputs",  f"{nombre_doc}.docx")

    template = DocxTemplate(ruta_plantilla)
    context = contexto
    template.render(context)
    template.save(ruta_salida)

