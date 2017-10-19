from peewee import *
from playhouse.db_url import connect

db = connect('mysql://root:secret@127.0.0.1:3306/o2o')

class BaseModel(Model):
    class Meta:
        database=db
class offline(BaseModel):
    User_id=CharField()
    Merchant_id=CharField()
    Coupon_id=CharField(null=True)
    Discount_rate=CharField(null=True)
    ###
    Rate=DoubleField(null=True)
    Satisfaction=IntegerField(null=True)
    Decrease=IntegerField(null=True)
    ###
    Distance=IntegerField(null=True)
    Date_received=DateField(null=True)
    Date=DateField(null=True)
class online(BaseModel):
    User_id = CharField()
    Merchant_id = CharField()
    Action=SmallIntegerField()
    Coupon_id = CharField(null=True)
    Discount_rate = CharField(null=True)
    ###
    Rate = DoubleField(null=True)
    Satisfaction = IntegerField(null=True)
    Decrease = IntegerField(null=True)
    ###
    Date_received = DateField(null=True)
    Date = DateField(null=True)
class samples(BaseModel):
    User_id=CharField()
    Merchant_id=CharField()
    Coupon_id=CharField()
    Discount_rate=CharField()
    ###
    Rate = DoubleField(null=True)
    Satisfaction = IntegerField(null=True)
    Decrease = IntegerField(null=True)
    ###
    Distance=IntegerField(null=True)
    Date_received=DateField()
