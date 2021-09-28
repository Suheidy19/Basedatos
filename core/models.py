from django.db import models
from django.db.models.enums import Choices

# Create your models here.
class Client(models.Model):
    firstname=models.CharField(max_length=50, verbose_name='Nombre(s)')
    Lastname1=models.CharField(max_length=50,verbose_name='Apellido Paterno')
    Lastname2=models.CharField(max_length=50,verbose_name='Apellido Materno')
    Age=models.IntegerField(verbose_name='Edad')
    CP=models.IntegerField(verbose_name='Codigo Postal')
    Location=models.CharField(max_length=50,verbose_name='Localidad')
    Street=models.CharField(max_length=50,verbose_name='Calle')
    Municipality=models.CharField(max_length=50,verbose_name='Municipio')
    State=models.CharField(max_length=50,verbose_name='Estado')
    Phone=models.CharField(max_length=15,verbose_name='Telefono')


    def __str__(self):
        return "{0} {1} {2}" .format(self.firstname, self.Lastname1, self.Lastname2)

    class Meta:
        verbose_name="Cliente"
        verbose_name_plural="Clientes"

class Doctor(models.Model):
    firstname=models.CharField(max_length=50, verbose_name='Nombre(s)')
    Lastname1=models.CharField(max_length=50,verbose_name='Apellido Paterno')
    Lastname2=models.CharField(max_length=50,verbose_name='Apellido Materno')
    Age=models.IntegerField(verbose_name='Edad')
    CP=models.IntegerField(verbose_name='Codigo Postal')
    Location=models.CharField(max_length=50,verbose_name='Localidad')
    Street=models.CharField(max_length=50,verbose_name='Calle')
    Municipality=models.CharField(max_length=50,verbose_name='Municipio')
    State=models.CharField(max_length=50,verbose_name='Estado')
    Phone=models.CharField(max_length=15,verbose_name='Telefono')

    def __str__(self):
        return "{0} {1} {2}" .format(self.firstname,self.Lastname1,self.Lastname2)

    class Meta:
        verbose_name="Medico"
        verbose_name_plural="Medicos"

class Vendor(models.Model):
    firstname=models.CharField(max_length=50, verbose_name='Nombre(s)')
    Lastname1=models.CharField(max_length=50,verbose_name='Apellido Paterno')
    Lastname2=models.CharField(max_length=50,verbose_name='Apellido Materno')
    Age=models.IntegerField(verbose_name='Edad')
    CP=models.IntegerField(verbose_name='Codigo Postal')
    Location=models.CharField(max_length=50,verbose_name='Localidad')
    Street=models.CharField(max_length=50,verbose_name='Calle')
    Municipality=models.CharField(max_length=50,verbose_name='Municipio')
    State=models.CharField(max_length=50,verbose_name='Estado')
    Phone=models.CharField(max_length=15,verbose_name='Telefono')
    
    def __str__(self):
        return "{0} {1} {2}" .format(self.firstname,self.Lastname1,self.Lastname2)

    class Meta:
        verbose_name="Vendedor"
        verbose_name_plural="Vendedores"

class Provider(models.Model):
    firstname=models.CharField(max_length=50, verbose_name='Nombre(s)')
    Lastname1=models.CharField(max_length=50,verbose_name='Apellido Paterno')
    Lastname2=models.CharField(max_length=50,verbose_name='Apellido Materno')
    Phone=models.CharField(max_length=15,verbose_name='Telefono')

    def __str__(self):
        return "{0} {1} {2}" .format(self.firstname,self.Lastname1,self.Lastname2)

    class Meta:
        verbose_name="Proveedor"
        verbose_name_plural="Proveedores"

class Service(models.Model):
    name=models.CharField(max_length=50 ,verbose_name="Nombre del servicio")

    def __str__(self):
        return "{0}" .format(self.name)

    class Meta:
        verbose_name="Servicio"
        verbose_name_plural="Servicios"


MASCOTTYPE=[('Felino','Felino'),('Canino','Canino'), ('Reptil','Reptil'), ('Ave','Ave'),('Animal de granja','Animal de granja'),('Roedor','Roedor')]


class Mascot(models.Model):
    name=models.CharField(max_length=50, verbose_name='Nombre(s)')
    race=models.CharField(max_length=50,verbose_name='Raza')
    Color=models.CharField(max_length=50,verbose_name='Color')
    Age=models.CharField(max_length=50,verbose_name='Edad')
    type=models.CharField(choices=MASCOTTYPE, verbose_name='Especie', max_length=20)
    Client=models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Cliente')

    def __str__(self):
        return "{0} {1}" .format(self.name,self.race)
    
    class Meta:
        verbose_name="Mascota"  
        verbose_name_plural="Mascotas"


class Product(models.Model):
    name=models.CharField(max_length=50, verbose_name='Nombre')
    quantity=models.IntegerField(verbose_name='Cantidad',)
    price=models.DecimalField(verbose_name='Precio', max_digits=5,decimal_places=2, default=0.00)
    Expiration=models.DateField(verbose_name='Fecha de Caducidad')
    Provider=models.ForeignKey(Provider,on_delete=models.CASCADE, verbose_name='Proveedor')

    def __str__(self):
        return "{0} {1}" .format(self.name,self.price,self.Provider)
    
    class Meta:
        verbose_name="Producto"  
        verbose_name_plural="Productos"

class Office(models.Model):
    name=models.CharField(max_length=50, verbose_name='Nombre')
    CP=models.IntegerField(verbose_name='Codigo Postal')
    Location=models.CharField(max_length=50,verbose_name='Localidad')
    Street=models.CharField(max_length=50,verbose_name='Calle')
    Municipality=models.CharField(max_length=50,verbose_name='Municipio')
    State=models.CharField(max_length=50,verbose_name='Estado')
    Phone=models.CharField(max_length=15,verbose_name='Telefono')

    def __str__(self):
        return "{0}" .format(self.name)
    
    class Meta:
        verbose_name="Sucursal"  
        verbose_name_plural="Sucursales"

class Cite(models.Model):
    date=models.DateField(verbose_name='Fecha de la cita')
    Service=models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Tipo de servicio')
    Doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE,verbose_name='Medico')
    Product=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='Producto')
    Client=models.ForeignKey(Client,on_delete=models.CASCADE,verbose_name='Cliente')

    def __str__(self):
        return "Fecha de la cita: {0}   Cliente: {1} " .format(self.date, self.Client)
    
    class Meta:
        verbose_name="Cita"  
        verbose_name_plural="Citas"



class Sale(models.Model):
    date=models.DateField(verbose_name='Fecha de la compra')
    Office=models.ForeignKey(Office,on_delete=models.CASCADE,verbose_name='Sucursal')
    Client=models.ForeignKey(Client,on_delete=models.CASCADE,verbose_name='Cliente')
    Product=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='Producto')

    def __str__(self):
        return "Fecha de la Venta: {0}   Cliente: {1} " .format(self.date, self.Client)
    
    class Meta:
        verbose_name="Venta"  
        verbose_name_plural="Ventas"
   




