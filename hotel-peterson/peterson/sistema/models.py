from django.db import models

# Create your models here.
class TipoHab(models.Model):
    id_tipo = models.PositiveSmallIntegerField(primary_key=True)
    tipo = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=20, decimal_places=2)
    cant_per = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return f"Tipo de habitación: {self.tipo} Precio de la habitación: {self.precio} Cantidad de personas: {self.cant_per}"

class Habitacion(models.Model):
    id_hab = models.PositiveSmallIntegerField(primary_key=True)
    id_tipo = models.ForeignKey(TipoHab, on_delete=models.PROTECT)
    hab_ocupada = models.BooleanField(default=False)
    piso = models.PositiveSmallIntegerField()
    numero_habitacion = models.PositiveSmallIntegerField()

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Habitacion'
        verbose_name_plural = 'Habitaciones'

    def __str__(self):
        return f"{self.id_hab} | Tipo: {self.id_tipo.tipo} | Hab. Ocupada: {self.hab_ocupada} | Piso: {self.piso}"

class Cliente(models.Model):   
    id_cli = models.PositiveSmallIntegerField(primary_key=True)
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    dni = models.PositiveSmallIntegerField()
    mail = models.EmailField(max_length=150)
    telefono = models.PositiveSmallIntegerField()
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return f"{self.nombre} ({self.dni})"

class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    id_hab = models.ForeignKey(Habitacion, on_delete=models.PROTECT, blank=True)
    id_cli = models.ForeignKey(Cliente, on_delete=models.PROTECT, blank=True)
    fecha_ing = models.DateTimeField()
    fecha_egr = models.DateTimeField()
    monto = models.DecimalField(decimal_places=2, max_digits=9)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'

    def __str__(self) -> str:
        tipo_habitacion = self.id_hab.id_tipo.tipo if self.id_hab else "N/A"
        return f"{self.id_cli.nombre} buscó {self.tipo_habitacion} para la fecha {self.fecha_ing} hasta {self.fecha_egr}"

class Puesto(models.Model):
    id_puesto = models.PositiveSmallIntegerField(primary_key=True)
    cargo = models.CharField(max_length=150)
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Puesto'
        verbose_name_plural = 'Puestos'
    
    def __str__(self):
        return f"{self.cargo}"

class Empleado(models.Model):
    id_emp = models.PositiveSmallIntegerField(primary_key=True)
    id_puesto = models.ForeignKey(Puesto, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.PositiveIntegerField()
    dni = models.PositiveIntegerField()
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
    
    def __str__(self):
        return f"{self.nombre} ({self.dni})"

class Usuario(models.Model):
    id_user = models.PositiveSmallIntegerField(primary_key=True)
    id_cli = models.ForeignKey(Cliente, on_delete= models.PROTECT)
    id_emp = models.ForeignKey(Empleado, on_delete= models.PROTECT)
    user = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    mail = models.EmailField(max_length=150)
    es_emp = models.BooleanField()
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        
    def __str__(self):
        return f"{self.user}"

class Caja(models.Model):
    id_caja = models.PositiveSmallIntegerField(primary_key=True)
    id_emp = models.ForeignKey(Empleado, on_delete= models.PROTECT)
    #Faltaría agregar la tabla de facturas para permitir que caja tenga
    #Una FK de Facturas
    #id_fac = models.ForeignKey(factura, on_delete=models.PROTECT)
    id_reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)

    class Meta:
        verbose_name =("Caja")
        verbose_name_plural =("Cajas")

    def __str__(self):
        return f"ID_Caja: {self.id_caja} \n ID_Empleado: {self.id_emp}\nID_Reserva: {self.id_reserva}"
