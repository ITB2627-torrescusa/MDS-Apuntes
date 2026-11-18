from time import sleep

# region Declaració de Funcions ----------
def recopilar_ingredients():
    print("Comprar al supermercat")
    sleep(1)
    print("Disposar-los sobre el marbre")
    sleep(1)

def cuinar_tallarines():
    print("Cuinat tallarines")
    simular_cuinar(15)
    print("FI Tallarines")

def cuinar_pastanagues():
    print("Cuinant pastanagues")
    simular_cuinar(5)
    print("FI Pastanagues")

def simular_cuinar(temps=3):
    for _ in range(temps):
        print(". ", end="", flush=True)
        sleep(0.5)
    print()
# endregion

# region INICI: Preparar fideus Yakisoba

recopilar_ingredients()
cuinar_tallarines()
cuinar_pastanagues()
# endregion