import requests
from param import GetParameters
import json

class Negotiations(GetParameters):
    def __init__(
        self,
        url,
        token,
        page=None,
        limit=20,
        order="created_at",
        direction="desc",
        name=None,
        win=None,
        user_id=None,
        closed_at=None,
        closed_at_period=None,
        created_at_period=None,
        prediction_date_period=None,
        start_date=None,
        end_date=None
    ):
        self.url = url
        super().__init__(token, page=page, limit=limit, order=order, direction=direction, name=name, win=win, user_id=user_id, closed_at=closed_at, closed_at_period=closed_at_period, created_at_period=created_at_period, prediction_date_period=prediction_date_period, start_date=start_date, end_date=end_date)
        
    def make_query(self):
        query_parts = [f"{key}={val}" for key, val in self.items.items() if val is not None]
        semi_final_str = "&".join(query_parts)
        query_str = "?" + semi_final_str
        return query_str
    
    def list_all(self):
        query = self.make_query()
        headers = {"accept":"application/json"}
        full_url = f"{self.url}{query}"
        try:
            req = requests.get(full_url, headers=headers)
        except Exception as e:
            print(f"Failed to fetch URL {full_url}. Error: {e}")
            return
        if req.status_code in [401, 403, 404]:
            print(f"{req.status_code} status code found.")
            return
        return req.text
    
    def show_negotiation(self, deal_id):
        query = f"?token={self.token}"
        headers = {"accept": "application/json"}
        full_url = f"{self.url}/{deal_id}{query}"
        try:
            req = requests.get(full_url, headers=headers)
        except Exception as e:
            print(f"Failed to fetch URL {full_url}. Error: {e}")
            return
        if req.status_code in [401, 403, 404]:
            print(f"{req.status_code} status code found.")
            return
        return req.text
        
        
class NegotiationParser:
    def __init__(self, negotiation_obj):
        self.negotiation_obj = negotiation_obj
        
    def parse_all_deals(self):
        response = json.loads(self.negotiation_obj.list_all())
        deals = response['deals']
        data = []
        for deal in deals:
            in_data = {}
            in_data['Tipo'] = deal.get('name')
            in_data['Valor Mensal'] = deal.get('amount_montly')
            in_data['Valor Único'] = deal.get('amount_unique')
            in_data['Projeção Anual'] = (deal.get('amount_montly', 0) * 12) + deal.get('amount_unique', 0) if deal.get('amount_montly', 0) != 0 else 0
            in_data['Iniciado em'] = deal.get('created_at')
            in_data['Empresa'] = {}
            in_data['Negociante'] = deal.get('organization', {}).get('user', {}).get('name')
            in_data['Nome da empresa'] = deal.get('organization', {}).get('name')
            in_data['Segmento'] = deal.get('organization_segments', {}).get('name')
            in_data['Estágio'] = deal.get('deal_stage', {}).get('name')
            in_data['Produtos negociados'] = []
            for product in deal['deal_products']:
                product_name = product.get('name')
                if not product_name in in_data['Produtos negociados']:
                    in_data['Produtos negociados'].append(product_name)
            
            data.append(in_data)
            
        return data
    
        
        
        
        
    