from wtforms.validators import ValidationError

class Unique(object):
    def __init__(self,model, field, message=u 'this element already exsists.'):
        self.model = model
        self.field = field
        
    def __call__(self, form, field):
        check = self.model.quely.filter(self.field == field.data).first()
        if check:
            raise ValidationError(self.message)