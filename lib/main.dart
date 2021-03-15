import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Covid 19 Vaccine Survey',
      theme: ThemeData(
        primarySwatch: Colors.teal,
      ),
      home: FormScreen(),
    );
  }
}

class FormScreen extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return FormScreenState();
  }
}

class FormScreenState extends State<FormScreen> {
  String _name;
  String _surname;
  DateTime birthDate = DateTime.now();
  String _cityValue;
  String _genderValue;
  String _vaccineTypeValue;
  String _sideEffectValue;

  bool nameFilled = false;
  bool surnameFilled = false;
  bool birthDateFilled = false;
  bool citySelected = false;
  bool genderSelected = false;
  bool vaccineTypeSelected = false;
  bool sideEffectSelected = false;

  List<String> sideEffects = [
    'None',
    'Headache',
    'Fatigue',
    'Fever',
    'Muscle pain',
    'Diarrhoea',
    'Pain at the injection site'
  ];
  List<String> vaccineTypes = [
    'Pfizer-BioNtech',
    'Sputnik V',
    'Oxford-Astra-Zeneca',
    'Sinovac',
    'Moderna',
    'Johnson-Johnson'
  ];
  List<String> cities = ['Ankara', 'İstanbul', 'İzmir'];
  List<String> genders = [
    'Male',
    'Female',
    'Non-binary',
  ];

  final GlobalKey<FormState> _formKey = GlobalKey<FormState>();

  Widget _buildName() {
    return TextFormField(
      decoration: InputDecoration(labelText: 'Name'),
      maxLength: 20,
      validator: (String value) {
        if (value.isEmpty) {
          return 'Name is Required';
        }
        return null;
      },
      onSaved: (String value) {
        _name = value;
      },
      onChanged: (String value) {
        setState(() {
          _name = value;
          nameFilled = true;
        });
      },
    );
  }

  Widget _buildSurname() {
    return TextFormField(
      decoration: InputDecoration(labelText: 'Surname'),
      maxLength: 20,
      validator: (String value) {
        if (value.isEmpty) {
          return 'Surname is Required';
        }
        return null;
      },
      onSaved: (String value) {
        _surname = value;
      },
      onChanged: (String value) {
        setState(
          () {
            _surname = value;
            surnameFilled = true;
          },
        );
      },
    );
  }

  Widget _buildBirthDate() {
    return InputDatePickerFormField(
      firstDate: DateTime(1920),
      lastDate: DateTime(2021),
      errorFormatText:
          "Input is in wrong format, please enter in dd/mm/yyyy format",
      errorInvalidText: "Entered date is invalid",
      fieldLabelText: "Please enter your birth date",
    );
  }

  Widget _buildBirthDateField() {
    return ElevatedButton(
        onPressed: () => _selectDate(context),
        child: Text('Select birth date'));
  }

  Future<Null> _selectDate(BuildContext context) async {
    final DateTime picked = await showDatePicker(
        context: context,
        initialDate: birthDate,
        firstDate: DateTime(1920, 8),
        lastDate: DateTime.now());
    if (picked != null && picked != birthDate)
      setState(() {
        birthDate = picked;
        birthDateFilled = true;
      });
  }

  Widget _buildCity() {
    return DropdownButtonFormField(
      validator: (String value) {
        if (value == null) {
          return 'City is required';
        }
        return null;
      },
      hint: _cityValue == null
          ? Text('City')
          : Text(
              _cityValue,
              style: TextStyle(color: Colors.blue),
            ),
      isExpanded: true,
      iconSize: 30.0,
      style: TextStyle(color: Colors.blue),
      items: cities.map(
        (val) {
          return DropdownMenuItem<String>(
            value: val,
            child: Text(val),
          );
        },
      ).toList(),
      onChanged: (val) {
        setState(
          () {
            _cityValue = val;
            citySelected = true;
          },
        );
      },
    );
  }

  Widget _buildGender() {
    return DropdownButtonFormField(
      validator: (String value) {
        if (value == null) {
          return 'Gender is required';
        }
        return null;
      },
      hint: _genderValue == null
          ? Text('Gender')
          : Text(
              _genderValue,
              style: TextStyle(color: Colors.blue),
            ),
      isExpanded: true,
      iconSize: 30.0,
      style: TextStyle(color: Colors.blue),
      items: genders.map(
        (val) {
          return DropdownMenuItem<String>(
            value: val,
            child: Text(val),
          );
        },
      ).toList(),
      onChanged: (val) {
        setState(
          () {
            _genderValue = val;
            genderSelected = true;
          },
        );
      },
    );
  }

  Widget _buildVaccineType() {
    return DropdownButtonFormField(
      validator: (String value) {
        if (value == null) {
          return 'Vaccine type is required';
        }
        return null;
      },
      hint: _vaccineTypeValue == null
          ? Text('Vaccine Type')
          : Text(
              _vaccineTypeValue,
              style: TextStyle(color: Colors.blue),
            ),
      isExpanded: true,
      iconSize: 30.0,
      style: TextStyle(color: Colors.blue),
      items: vaccineTypes.map(
        (val) {
          return DropdownMenuItem<String>(
            value: val,
            child: Text(val),
          );
        },
      ).toList(),
      onChanged: (val) {
        setState(
          () {
            _vaccineTypeValue = val;
            vaccineTypeSelected = true;
          },
        );
      },
    );
  }

  Widget _buildSideEffect() {
    return DropdownButtonFormField(
      validator: (String value) {
        if (value == null) {
          return 'Side effect is required';
        }
        return null;
      },
      hint: _sideEffectValue == null
          ? Text('Side Effects')
          : Text(
              _sideEffectValue,
              style: TextStyle(color: Colors.blue),
            ),
      isExpanded: true,
      iconSize: 30.0,
      style: TextStyle(color: Colors.blue),
      items: sideEffects.map(
        (val) {
          return DropdownMenuItem<String>(
            value: val,
            child: Text(val),
          );
        },
      ).toList(),
      onChanged: (val) {
        setState(
          () {
            _sideEffectValue = val;
            sideEffectSelected = true;
          },
        );
      },
    );
  }

  Widget _buildSubmitButton() {
    return Visibility(
      visible: nameFilled &&
          surnameFilled &&
          birthDateFilled &&
          citySelected &&
          genderSelected &&
          vaccineTypeSelected &&
          sideEffectSelected,
      child: ElevatedButton(
        child: Text(
          'Submit',
          style: TextStyle(color: Colors.white, fontSize: 16),
        ),
        onPressed: () {
          if (!_formKey.currentState.validate()) {
            return;
          }
          _formKey.currentState.save();
          print(_name);
          print(_surname);
          //print(_birthDate.toString());
          print(birthDate.toString());
          print(_cityValue);
          print(_genderValue);
          print(_vaccineTypeValue);
          print(_sideEffectValue);
          //Send to API
        },
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(
          "Covid19 Vaccine Survey",
          style: TextStyle(
            fontSize: 25.0,
            fontWeight: FontWeight.bold,
            letterSpacing: 2.0,
            color: Colors.white70,
          ),
        ),
        centerTitle: true,
        backgroundColor: Colors.red[600],
      ),
      body: SingleChildScrollView(
        child: Container(
          margin: EdgeInsets.all(24),
          child: Form(
            key: _formKey,
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                _buildName(),
                _buildSurname(),
                _buildBirthDateField(),
                //_buildBirthDate(),
                _buildCity(),
                _buildGender(),
                _buildVaccineType(),
                _buildSideEffect(),
                _buildSubmitButton(),
                SizedBox(height: 100),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
