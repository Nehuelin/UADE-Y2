# CONCIERTO EN FRAILE MUERTO

# ESTRATEGIA: Par conocer todas las distintas configuraciones posibles para el concierto, se puede aplicar programacion dinamica de la siguiente manera:
# Se crea una lista que tendra n elementos (siendo n la cantidad de alumnos). En esa lista se aplicara la siguiente formula:
# Si n = 0, significa que no hay alumnos, por ende no habra ninguna configuracion
# Si n = 1, habrá un alumno. Por lo tanto, tocará solo (es decir, una configuracion)
# Si n = 2, habrá dos alumnos, por lo que habran dos configuraciones 
# Para el resto de los alumnos n > 2, se utilizará la combinacion de las configuraciones de los casos n - 1 y n - 2. La formula para este caso seria M[i] = M[i - 1] + (i - 1)*M[i - 2]

# ALGORITMO contarConfiguraciones(n: entero){
#   M = nuevo Vector(n + 1)
#   para i = 0 hasta len(Vector){
#        si (i == 0){
#           M[i] = 0       
#       } sino si (i == 1) {
#           M[i] = 1
#       } sino si (i == 2) {
#           M[i] = 2
#       } sino {
#           M[i][j] = M[i - 1] + ((i - 1) * M[i - 2])
#       }
#   }
#   devuelve M[n]
#
# COSTO: Lineal O(n), siendo n la cantidad de alumnos

def contar_configuraciones(n: int):
    M = [0] * (n+1)
    for i in range(len(M)):
        if i == 0:
            M[i] = 0
        elif i == 1:
            M[i] = 1
        elif i == 2:
            M[i] = 2
        else:
            M[i] = M[i-1] + ((i - 1) * M[i-2])
    
    return M[n]

print(contar_configuraciones(4))

