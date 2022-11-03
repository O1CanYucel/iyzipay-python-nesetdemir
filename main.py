from iyzipay import iyzipay_resource


class IyzicoAddress():
    contactName = "Ömer Can Yücel"
    city = "İstanbul"
    country = "Turkey"
    address = "İTÜ MAGNET Maslak"
    zipCode = 34732

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __dict__(self):
        return {
            "contactName": self.contactName,
            "city": self.city,
            "country": self.country,
            "address": self.address,
            "zipCode": self.zipCode,
        }


class IyzicoCustomer():
    name = "Ömer Can"
    surname = "Yücel"
    email = "omer.yucel@earnado.com"
    gsmNumber = "+905357628668"
    identityNumber = "11111111111"
    billingAddress = IyzicoAddress().__dict__()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __dict__(self):
        return {
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
            "gsmNumber": self.gsmNumber,
            "identityNumber": self.identityNumber,
            "billingAddress": self.billingAddress,
        }


class IyzicoCheckoutFormRequest():
    locale = "tr"
    conversationId = "123"
    projectId = 209
    callbackUrl = "https://dev.api.mikrolo.com/iyzico/callback/"
    pricingPlanReferenceCode = "d20b5444-4151-4421-ad39-e7e1721d43a9"
    subscriptionInitialStatus = "ACTIVE"
    customer = IyzicoCustomer().__dict__()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __dict__(self):
        return {
            "locale": self.locale,
            "conversationId": self.conversationId,
            "projectId": self.projectId,
            "callbackUrl": self.callbackUrl,
            "pricingPlanReferenceCode": self.pricingPlanReferenceCode,
            "subscriptionInitialStatus": self.subscriptionInitialStatus,
            "customer": self.customer,
        }


class IyzicoCheckoutFormResultRequest(object):
    def __init__(self, token):
        self.token = token

    def __dict__(self):
        return {
            "token": self.token,
        }


options = {
    "apiKey": "J9tBaujBZzk8XbtrQ5uWTb1rV8kRZ6IM",
    "secretKey": "62dFw2ZTAKhmFWYhwwi7PtDThDUO2iBm",
    "baseUrl": "api.iyzipay.com"
    }


class main:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


def get_checkout_form(request: IyzicoCheckoutFormRequest):
    checkout_form = iyzipay_resource.SubscriptionCheckoutForm().create(request=request, options=options)
    return checkout_form.read().decode('utf-8')


def get_checkout_form_result(request: IyzicoCheckoutFormRequest):
    result = iyzipay_resource.SubscriptionCheckoutForm().get(request=request, options=options)
    return result.read().decode('utf-8')


result = get_checkout_form_result(IyzicoCheckoutFormResultRequest(token="e89e4df8-1ee4-4a8f-b133-379bbd47a8d2").__dict__())
print(result)
