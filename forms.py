from email.policy import default
from time import daylight
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, DecimalField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class AccidentForm(FlaskForm):
    street1= StringField('Street 1', validators=[DataRequired(), Length(min=1, max=100)])
    street2= StringField('Street 2', validators=[DataRequired(), Length(min=1, max=100)])
    month = SelectField('Month', validators=[DataRequired()], choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')])
    day = SelectField('Day', validators=[DataRequired()], choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31')])
    hour = SelectField('Hour', validators=[DataRequired()], choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24')])
    district = SelectField('Disctrict', validators=[DataRequired()], choices=[('Toronto and East York', 'Toronto and East York')])
    latitude = DecimalField('Lattitude', validators=[DataRequired()])
    longitude = DecimalField('Longitude', validators=[DataRequired()])
    visibility = SelectField('Visibility', validators=[DataRequired()], choices=[('Clear', 'Clear'), ('Rain', 'Rain'), ('Snow', 'Snow'), ('Fog', 'Fog'),  ('Dust', 'Dust'), ('Mist', 'Mist'), ('Smoke', 'Smoke'), ('Strong wind', 'Strong Wind'), ('Drifting Snow', 'Drifting Snow'), ('Freezing Rain', 'Freezing Rain'), ('Other', 'Other')])
    light = SelectField('Light', validators=[DataRequired()], choices=[('Daylight', 'Daylight'), ('Daylight, artificial', 'Daylight, artificial'), ('Dark', 'Dark'), ('Dark, artificial', 'Dark, artificial'), ('Dawn', 'Dawn'), ('Dawn, artificial', 'Dawn, artificial'), ('Dusk', 'Dusk'), ('Dusk, artificial', 'Dusk, artificial')])
    injury = SelectField('Injury', validators=[DataRequired()], choices=[('None', 'None'), ('Minimal', 'Minimal'), ('Minor', 'Minor'), ('Major', 'Major'), ('Fatal', 'Fatal')])
    pedestrian = BooleanField('Pedestrian', validators=[DataRequired()])
    cyclist = BooleanField('Cyclist', validators=[DataRequired()])
    automobile = BooleanField('Automobile', validators=[DataRequired()])
    motorcycle = BooleanField('Motorcycle', validators=[DataRequired()])
    truck = BooleanField('Truck', validators=[DataRequired()])
    transit_vehicle = BooleanField('Transit Vehicle', validators=[DataRequired()])
    emergency_vehicle = BooleanField('Emergency Vehicle', validators=[DataRequired()])
    passenger = BooleanField('Passenger', validators=[DataRequired()])
    speeding = BooleanField('Speeding', validators=[DataRequired()])
    aggressive_driver = BooleanField('Aggressive Driver', validators=[DataRequired()])
    redlight = BooleanField('Redlight', validators=[DataRequired()])
    alcohol = BooleanField('Alcohol', validators=[DataRequired()])
    disability = BooleanField('Disability', validators=[DataRequired()])
    models = SelectField('Models', validators=[DataRequired()], choices=[])



