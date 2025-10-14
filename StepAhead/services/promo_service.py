from app import db

class Promotion(db.Model):
    __tablename__ = "promotions"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    discount = db.Column(db.Integer, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    category = db.Column(db.String(100), nullable=False)  # задължително
    subcategory = db.Column(db.String(100), nullable=False)  # задължително

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "discount": self.discount,
            "start": self.start_date.isoformat(),
            "end": self.end_date.isoformat(),
            "category": self.category,
            "subcategory": self.subcategory
        }


def get_all_promotions():
    return Promotion.query.all()

def add_promotion(title, description, discount, start_date, end_date, category, subcategory):
    promo = Promotion(
        title=title,
        description=description,
        discount=discount,
        start_date=start_date,
        end_date=end_date,
        category=category,
        subcategory=subcategory
    )
    db.session.add(promo)
    db.session.commit()
    return promo

def delete_promotion(promo_id):
    promo = Promotion.query.get(promo_id)
    if not promo:
        return False
    db.session.delete(promo)
    db.session.commit()
    return True