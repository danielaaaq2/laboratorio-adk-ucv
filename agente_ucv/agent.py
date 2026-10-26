import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()


from google.adk.agents.llm_agent import Agent

def explicar_concepto(concepto: str) -> dict:
    """Explica conceptos técnicos clave de ingeniería de software."""
    conceptos = {
        # Conceptos iniciales
        "api": "Una API permite la comunicación estructurada entre diferentes aplicaciones informáticas.",
        "algoritmo": "Un algoritmo es una secuencia finita y ordenada de instrucciones para resolver un problema.",
        "base de datos": "Una base de datos almacena y organiza información para su rápida recuperación.",
        
        # 5 Nuevos conceptos técnicos agregados para el reto
        "docker": "Docker empaqueta aplicaciones y sus dependencias en contenedores ligeros y portables.",
        "pipeline": "Un pipeline es una secuencia automatizada de pasos de integración y despliegue continuo (CI/CD).",
        "scrum": "Scrum es un marco de trabajo ágil iterativo centrado en entregas incrementales de valor.",
        "git": "Git es un sistema de control de versiones distribuido para rastrear cambios en el código fuente.",
        "kubernetes": "Kubernetes es una plataforma de orquestación para automatizar el despliegue de contenedores."
    }
    
    # Validación de entrada
    if not concepto or not isinstance(concepto, str):
        return {
            "status": "error",
            "mensaje": "Debes proporcionar una cadena de texto válida."
        }
        
    concepto = concepto.lower().strip()
    if concepto in conceptos:
        return {
            "status": "success",
            "explicacion": conceptos[concepto]
        }
    return {
        "status": "not_found",
        "explicacion": "Concepto técnico no registrado en el repositorio del agente."
    }

def calcular_promedio(numeros: list) -> dict:
    """Calcula el promedio de una lista de notas o números con validación estricta de entrada."""
    # Validación de entrada: verificar que sea una lista no vacía
    if not isinstance(numeros, list) or len(numeros) == 0:
        return {
            "status": "error",
            "mensaje": "Error de entrada: Se requiere una lista no vacía de números."
        }
    
    # Validación de entrada: verificar que todos los elementos sean numéricos
    for n in numeros:
        if not isinstance(n, (int, float)):
            return {
                "status": "error",
                "mensaje": "Error de entrada: Todos los elementos dentro de la lista deben ser números."
            }
        if n < 0 or n > 20:
            return {
                "status": "error",
                "mensaje": "Error de entrada: Las notas deben estar dentro del rango numérico de 0 a 20."
            }

    promedio = sum(numeros) / len(numeros)
    return {
        "status": "success",
        "cantidad_elementos": len(numeros),
        "promedio": round(promedio, 2)
    }

root_agent = Agent(
    model="gemini-3.8-flash",
    name="agente_ucv",
    description="Agente académico oficial UCV para ingeniería de sistemas",
    instruction="""
    Eres un asistente académico universitario oficial de la UCV.
    Responde de forma concisa, educada y profesional en español.
    Utiliza las herramientas disponibles para explicar conceptos o calcular promedios.
    """,
    tools=[explicar_concepto, calcular_promedio],
)