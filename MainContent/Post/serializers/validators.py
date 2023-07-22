
from django.core.validators import  MaxValueValidator

class SizeValidator(MaxValueValidator):
    #Rewritting the MaxValueValidator from django in order to adapted to the current situation
    
    def __call__(self, value):
        cleaned = self.clean(value)
        limit_value = self.limit_value() if callable(self.limit_value) else self.limit_value
        if self.compare(cleaned.size, limit_value):
            raise ValidationError(f"Ensure this file '{cleaned.name}' is less or equal than {limit_value/1000000} MB", code=self.code)