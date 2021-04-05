import my_iterator as mi

def run():
    o = mi.IncolumeDevices0()
    try:
        print("Chamada ao metodo 'len'")

        print(f"{o.__class__.__name__} possue {len(o)} dispositivos")
    except TypeError as e:
        print(f"Ops: {e}")

    o = mi.IncolumeDevices1()
    try:
        print("\n\nCorreção da chamada ao metodo 'len'")
        print(f"{o.__class__.__name__} possue {len(o)} dispositivos")
    except TypeError as e:
        print(f"Ops: {e}")

    try:
        print("\nExtrair dispositivo da lista")
        print(f"{o.__class__.__name__}: {o[0]} dispositivos")
    except TypeError as e:
        print(f"Ops: {e}")

    o = mi.IncolumeDevices2()
    try:
        print("\nCorreção Extrair 1º dispositivo da lista")
        print(f"{o.__class__.__name__}: {o[0]} dispositivos")
        print(f"{o.__class__.__name__}: {len(o)} dispositivos")
    except TypeError as e:
        print(f"Ops: {e}")
    try:
        print("\nCorreção Extrair ultimo dispositivo da lista")
        print(f"{o.__class__.__name__}: {o[-1]} dispositivos")
        print(f"{o.__class__.__name__}: {len(o)} dispositivos")
    except TypeError as e:
        print(f"Ops: {e}")
    try:
        print("\nCorreção Extrair dispositivo ausente da lista")
        print(f"{o.__class__.__name__}: {o['a']} dispositivos")
    except TypeError as e:
        print(f"Ops: {e}")

    print("\nChecar dispositivo da lista")
    if 'nokia 1600 GSM' in o:
        print("dispositivos encontrado")
    else:
        print("dispositivos não encontrado")
    print(f"{o.__class__.__name__}: {len(o)} dispositivos")  # losted devs

    o = mi.IncolumeDevices3()
    print("\nCorreção em checar dispositivo da lista")
    if 'nokia 1600 GSM' in o:
        print("dispositivos encontrado")
    else:
        print("dispositivos não encontrado")
    print(f"{o.__class__.__name__}: {len(o)} dispositivos")  # not losted devs

    print("\nIterrar sobre os dispositivos da lista")
    for dev in o:
        print(dev)
    print(f"{o.__class__.__name__}: {len(o)} dispositivos")    # losted devs again

    o = mi.IncolumeDevices4()
    print("\nCorreção Iterrar sobre os dispositivos da lista")
    e = []
    for dev in o:
        print(dev)
        e.append(dev)
    print(f"{o.__class__.__name__}: {len(o)} dispositivos")    # losted devs again


if __name__ == "__main__":
    run()
