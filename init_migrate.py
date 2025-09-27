# Script para inicializar Alembic y migrar la base de datos automáticamente
import os
import shutil
import subprocess

alembic_dir = os.path.join(os.getcwd(), 'alembic')

# 1. Borra la carpeta alembic/ si existe
if os.path.exists(alembic_dir):
    shutil.rmtree(alembic_dir)

# 2. Inicializa Alembic
def run(cmd):
    print(f"Ejecutando: {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        raise Exception(f"Error ejecutando: {cmd}")

run("alembic init alembic")

# 3. Copia tu env.py personalizado si existe backup
if os.path.exists('env.py.bak'):
    shutil.copy('env.py.bak', os.path.join(alembic_dir, 'env.py'))

# 4. Crea la migración inicial y aplica
run("alembic revision --autogenerate -m 'init'")
run("alembic upgrade head")

print("Migración completada. Ahora puedes correr los tests.")
