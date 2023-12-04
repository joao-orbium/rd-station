
class GetParameters:
    def __init__(
        self,
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
        self.token = token
        self.page = page
        self.limit = limit
        self.order = order
        self.direction = direction
        self.name = name
        self.win = win
        self.user_id = user_id
        self.closed_at = closed_at
        self.closed_at_period = closed_at_period
        self.created_at_period = created_at_period
        self.prediction_date_period = prediction_date_period
        self.start_date = start_date
        self.end_date = end_date
        self.items = {
            "token": self.token,
            "page": self.page,
            "limit": self.limit,
            "order": self.order,
            "direction": self.direction,
            "name": self.name,
            "win": self.win,
            "user_id": self.user_id,
            "closed_at": self.closed_at,
            "closed_at_period": self.closed_at_period,
            "created_at_period": self.created_at_period,
            "prediction_date_period": self.prediction_date_period,
            "start_date": self.start_date,
            "end_date": self.end_date
        }
        