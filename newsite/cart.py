from .models import Service


class Cart():
    def __init__(self, request_session):
        self.request_session = request_session
        if 'service_dict' not in self.request_session:
            self.request_session['service_dict'] = {}
        self.request_session.save()

    def add_service(self, service_id):
        service_dict = self.request_session.get('service_dict')
        if str(service_id) in service_dict:
            service_count = service_dict.get(str(service_id))
            service_dict[str(service_id)] = service_count + 1
        else:
            service_dict[str(service_id)] = 1
        self.request_session['service_dict'] = service_dict
        print(service_dict)
        self.request_session.save()

    def del_service(self, service_id):
        service_dict = self.request_session.get('service_dict')
        service_count = service_dict.get(str(service_id))
        if service_count > 1:
            service_count -= 1
            service_dict[str(service_id)] = service_count
        elif service_count == 1:
            service_dict.pop(str(service_id))
        self.request_session['service_dict'] = service_dict
        self.request_session.save()

    def view_service(self):
        return self.request_session.get('service_dict')

    def total_cost(self):
        total_cost = 0
        service_dict = self.request_session.get('service_dict')
        for i in service_dict.keys():
            cost = Service.objects.get(pk=i).service_price
            count = service_dict.get(i)
            total_cost += (cost * count)
        return total_cost

    def del_all_service(self):
        service_dict = {}
        self.request_session['service_dict'] = service_dict
        self.request_session.save()
