counter = 1
for k, v in preoutput['dir']['flash:/']['files'].items():
    try:
        print (f"{counter} - {k}")
        counter += 1
    except AttributeError:
        pass
print(f"""
===============================================================
{counter-1} files were found in flash.
===============================================================\n""")
