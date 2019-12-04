def custom500(error):
    print('entro')
    return type(error)

handler = {
    500: custom500,
}
