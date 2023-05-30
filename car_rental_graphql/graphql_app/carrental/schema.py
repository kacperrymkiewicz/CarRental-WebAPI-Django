import graphene
from graphene_django import DjangoObjectType
from .models import Car, Customer, Rental


class CarType(DjangoObjectType):
    class Meta:
        model = Car
        fields = ('id', 'brand', 'model', 'type', 'production_year', 'price', 'registration_plate')


class CustomerType(DjangoObjectType):
    class Meta:
        model = Customer
        fields = ('id', 'firstname', 'lastname', 'phone_number', 'zip_code', 'city', 'street', 'house_number')


class RentalType(DjangoObjectType):
    class Meta:
        model = Rental
        fields = ('id', 'pickup_date', 'return_date', 'customer', 'car')


class Query(graphene.ObjectType):
    cars = graphene.List(CarType)
    customers = graphene.List(CustomerType)
    rentals = graphene.List(RentalType)

    def resolve_cars(root, info, **kwargs):
        return Car.objects.all()

    def resolve_customers(root, info, **kwargs):
        return Customer.objects.all()

    def resolve_rentals(root, info, **kwargs):
        return Rental.objects.all()


class CarInput(graphene.InputObjectType):
    brand = graphene.String()
    model = graphene.String()
    type = graphene.String()
    production_year = graphene.Int()
    price = graphene.Float()
    registration_plate = graphene.String()


class CreateCar(graphene.Mutation):
    class Arguments:
        input = CarInput(required=True)

    car = graphene.Field(CarType)

    @classmethod
    def mutate(cls, root, info, input):
        car = Car()
        car.brand = input.brand
        car.model = input.model
        car.type = input.type
        car.production_year = input.production_year
        car.price = input.price
        car.registration_plate = input.registration_plate
        car.save()
        return CreateCar(car=car)


class UpdateCar(graphene.Mutation):
    class Arguments:
        input = CarInput(required=True)
        id = graphene.ID()

    car = graphene.Field(CarType)

    @classmethod
    def mutate(cls, root, info, input, id):
        car = Car.objects.get(pk=id)
        car.brand = input.brand
        car.model = input.model
        car.type = input.type
        car.production_year = input.production_year
        car.price = input.price
        car.registration_plate = input.registration_plate
        car.save()

        return UpdateCar(car=car)


class DeleteCar(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    car = graphene.Field(CarType)

    @classmethod
    def mutate(cls, root, info, id):
        car = Car.objects.get(pk=id)
        car.delete()

        return DeleteCar(car=car)


class CustomerInput(graphene.InputObjectType):
    firstname = graphene.String()
    lastname = graphene.String()
    phone_number = graphene.String()
    zip_code = graphene.String()
    city = graphene.String()
    street = graphene.String()
    house_number = graphene.String()


class CreateCustomer(graphene.Mutation):
    class Arguments:
        input = CustomerInput(required=True)

    customer = graphene.Field(CustomerType)

    @classmethod
    def mutate(cls, root, info, input):
        customer = Customer()
        customer.firstname = input.firstname
        customer.lastname = input.lastname
        customer.phone_number = input.phone_number
        customer.zip_code = input.zip_code
        customer.city = input.city
        customer.street = input.street
        customer.house_number = input.house_number
        customer.save()
        return CreateCustomer(customer=customer)


class UpdateCustomer(graphene.Mutation):
    class Arguments:
        input = CustomerInput(required=True)
        id = graphene.ID()

    customer = graphene.Field(CustomerType)

    @classmethod
    def mutate(cls, root, info, input, id):
        customer = Customer.objects.get(pk=id)
        customer.firstname = input.firstname
        customer.lastname = input.lastname
        customer.phone_number = input.phone_number
        customer.zip_code = input.zip_code
        customer.city = input.city
        customer.street = input.street
        customer.house_number = input.house_number
        customer.save()
        return UpdateCustomer(customer=customer)


class DeleteCustomer(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    customer = graphene.Field(CustomerType)

    @classmethod
    def mutate(cls, root, info, id):
        customer = Customer.objects.get(pk=id)
        customer.delete()

        return DeleteCustomer(customer=customer)


class RentalInput(graphene.InputObjectType):
    pickup_date = graphene.Date()
    return_date = graphene.Date()
    customer = graphene.Int()
    car = graphene.Int()


class CreateRental(graphene.Mutation):
    class Arguments:
        input = RentalInput(required=True)

    rental = graphene.Field(RentalType)

    @classmethod
    def mutate(cls, root, info, input):
        rental = Rental()
        rental.pickup_date = input.pickup_date
        rental.return_date = input.return_date
        rental.customer = input.customer
        rental.car = input.car
        rental.save()
        return CreateRental(rental=rental)


class UpdateRental(graphene.Mutation):
    class Arguments:
        input = RentalInput(required=True)
        id = graphene.ID()

    rental = graphene.Field(CustomerType)

    @classmethod
    def mutate(cls, root, info, input, id):
        rental = Rental.objects.get(pk=id)
        rental.pickup_date = input.pickup_date
        rental.return_date = input.return_date
        rental.customer = input.customer
        rental.car = input.car
        rental.save()
        return UpdateRental(rental=rental)


class Mutation(graphene.ObjectType):
    create_car = CreateCar.Field()
    update_car = UpdateCar.Field()
    delete_car = DeleteCar.Field()
    create_customer = CreateCustomer.Field()
    update_customer = UpdateCustomer.Field()
    delete_customer = DeleteCustomer.Field()
    create_rental = CreateRental.Field()
    update_rental = UpdateRental.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
