import json
def is_complex_num(objct):
    if '__complex__' in objct:
        return complex(objct['real'], objct['img'])

complex_object =json.loads('{"__complex__": true, "real": 4, "img": 5}', object_hook = is_complex_num)
print("Complex_object: ",complex_object)
