from simple_rest_client.resource import Resource


class CustomerResource(Resource):
    actions = {
        'list': {
            'method': 'GET',
            'url': 'customers'
        },
        'create': {
            'method': 'POST',
            'url': 'customers'
        },
        'retrieve': {
            'method': 'GET',
            'url': 'customers/{}',
        },
        'update': {
            'method': 'PUT',
            'url': 'customers/{}',
        },
        'destroy': {
            'method': 'DELETE',
            'url': 'customers/{}',
        },
    }


class PlanResource(Resource):
    actions = {
        'list': {
            'method': 'GET',
            'url': 'plans'
        },
        'create': {
            'method': 'POST',
            'url': 'plans'
        },
        'retrieve': {
            'method': 'GET',
            'url': 'plans/{}',
        },
        'update': {
            'method': 'PUT',
            'url': 'plans/{}',
        }
    }


class ProductResource(Resource):
    actions = {
        'list': {
            'method': 'GET',
            'url': 'products'
        },
        'create': {
            'method': 'POST',
            'url': 'products'
        },
        'retrieve': {
            'method': 'GET',
            'url': 'products/{}',
        },
        'update': {
            'method': 'PUT',
            'url': 'products/{}',
        }
    }


class PaymentMethodResource(Resource):
    actions = {
        'list': {
            'method': 'GET',
            'url': 'payment_methods'
        },
        'retrieve': {
            'method': 'GET',
            'url': 'payment_methods/{}',
        }
    }


class DiscountResource(Resource):
    actions = {
        'create': {
            'method': 'POST',
            'url': 'discounts'
        },
        'retrieve': {
            'method': 'GET',
            'url': 'discounts/{}',
        },
        'destroy': {
            'method': 'DELETE',
            'url': 'discounts/{}',
        },
    }


class SubscriptionResource(Resource):
    actions = {
        'list': {
            'method': 'GET',
            'url': 'subscriptions'
        },
        'create': {
            'method': 'POST',
            'url': 'subscriptions'
        },
        'retrieve': {
            'method': 'GET',
            'url': 'subscriptions/{}',
        },
        'update': {
            'method': 'PUT',
            'url': 'subscriptions/{}',
        },
        'destroy': {
            'method': 'DELETE',
            'url': 'subscriptions/{}',
        },
        'renew': {
            'method': 'POST',
            'url': 'subscriptions/{}/renew',
        },
        'reactivate': {
            'method': 'POST',
            'url': 'subscriptions/{}/reactivate',
        },
    }


class ProductItemResource(Resource):
    actions = {
        'create': {
            'method': 'POST',
            'url': 'product_items'
        },
        'retrieve': {
            'method': 'GET',
            'url': 'product_items/{}',
        },
        'update': {
            'method': 'PUT',
            'url': 'product_items/{}',
        },
        'destroy': {
            'method': 'DELETE',
            'url': 'product_items/{}',
        },
    }


class PeriodResource(Resource):
    actions = {
        'list': {
            'method': 'GET',
            'url': 'periods'
        },
        'retrieve': {
            'method': 'GET',
            'url': 'periods/{}',
        },
        'update': {
            'method': 'PUT',
            'url': 'periods/{}',
        },
        'bill': {
            'method': 'POST',
            'url': 'periods/{}/bill',
        },
    }


class BillResource(Resource):
    actions = {
        'list': {
            'method': 'GET',
            'url': 'bills'
        },
        'create': {
            'method': 'POST',
            'url': 'bills'
        },
        'retrieve': {
            'method': 'GET',
            'url': 'bills/{}',
        },
        'update': {
            'method': 'PUT',
            'url': 'bills/{}',
        },
        'destroy': {
            'method': 'DELETE',
            'url': 'bills/{}',
        },
        'approve': {
            'method': 'POST',
            'url': 'bills/{}/approve',
        },
        'charge': {
            'method': 'POST',
            'url': 'bills/{}/charge',
        },
    }


class BillItemResource(Resource):
    actions = {
        'retrieve': {
            'method': 'GET',
            'url': 'bill_items/{}',
        },
    }


class ChargeResource(Resource):
    actions = {
        'list': {
            'method': 'GET',
            'url': 'charges'
        },
        'retrieve': {
            'method': 'GET',
            'url': 'charges/{}',
        },
        'update': {
            'method': 'PUT',
            'url': 'charges/{}',
        },
        'destroy': {
            'method': 'DELETE',
            'url': 'charges/{}',
        },
        'reissue': {
            'method': 'POST',
            'url': 'charges/{}/reissue',
        },
        'charge': {
            'method': 'POST',
            'url': 'charges/{}/charge',
        },
        'refund': {
            'method': 'POST',
            'url': 'charges/{}/refund',
        },
        'fraud_review': {
            'method': 'POST',
            'url': 'charges/{}/fraud_review',
        },
    }


class TransactionResource(Resource):
    actions = {
        'list': {
            'method': 'GET',
            'url': 'transactions'
        },
        'create': {
            'method': 'POST',
            'url': 'transactions'
        },
        'retrieve': {
            'method': 'GET',
            'url': 'transactions/{}',
        },
        'update': {
            'method': 'PUT',
            'url': 'transactions/{}',
        },
    }


class PaymentProfileResource(Resource):
    actions = {
        'list': {
            'method': 'GET',
            'url': 'payment_profiles'
        },
        'create': {
            'method': 'POST',
            'url': 'payment_profiles'
        },
        'retrieve': {
            'method': 'GET',
            'url': 'payment_profiles/{}',
        },
        'destroy': {
            'method': 'DELETE',
            'url': 'payment_profiles/{}',
        },
        'verify': {
            'method': 'POST',
            'url': 'payment_profiles/{}/verify',
        },
    }


class UsageResource(Resource):
    actions = {
        'create': {
            'method': 'POST',
            'url': 'usages'
        },
        'destroy': {
            'method': 'DELETE',
            'url': 'usages/{}',
        },
    }


class InvoiceResource(Resource):
    actions = {
        'list': {
            'method': 'GET',
            'url': 'invoices'
        },
        'create': {
            'method': 'POST',
            'url': 'invoices'
        },
        'retrieve': {
            'method': 'GET',
            'url': 'invoices/{}',
        },
        'destroy': {
            'method': 'DELETE',
            'url': 'invoices/{}',
        },
        'retry': {
            'method': 'POST',
            'url': 'invoices/{}/retry',
        },
    }


class MovementResource(Resource):
    actions = {
        'create': {
            'method': 'POST',
            'url': 'movements'
        },
    }


class MessageResource(Resource):
    actions = {
        'list': {
            'method': 'GET',
            'url': 'messages'
        },
        'create': {
            'method': 'POST',
            'url': 'messages'
        },
        'retrieve': {
            'method': 'GET',
            'url': 'messages/{}',
        },
    }


class ImportBatchResource(Resource):
    actions = {
        'list': {
            'method': 'GET',
            'url': 'import_batches'
        },
        'create': {
            'method': 'POST',
            'url': 'import_batches'
        },
        'retrieve': {
            'method': 'GET',
            'url': 'import_batches/{}',
        },
    }


class MerchantResource(Resource):
    actions = {
        'list': {
            'method': 'GET',
            'url': 'merchant'
        },
    }


class IssueResource(Resource):
    actions = {
        'list': {
            'method': 'GET',
            'url': 'issues'
        },
        'retrieve': {
            'method': 'GET',
            'url': 'issues/{}',
        },
        'update': {
            'method': 'PUT',
            'url': 'issues/{}',
        },
    }
