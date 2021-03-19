import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'dart:convert';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      routes: {
        SecondPage.routeName: (context) => SecondPage(),
      },
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
  String regExp = r'^[a-z A-Z]+$';
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
  List<String> cities = [
    'Ankara',
    'İstanbul',
    'İzmir',
    'Adana',
    'Adıyaman',
    'Afyonkarahisar',
    'Ağrı'
  ];
  List<String> genders = [
    'Male',
    'Female',
    'Non-binary',
  ];

  final GlobalKey<FormState> _formKey = GlobalKey<FormState>();

  List _cities = [];
  // Fetch content from the json file
  Future<void> readJson() async {
    final String response =
        await rootBundle.loadString('json/cities_of_turkey.json');
    final data = await json.decode(response);
    setState(() {
      _cities = data["items"];
    });
    print(cities);
  }

  Widget _buildName() {
    return TextFormField(
      decoration: InputDecoration(labelText: 'Name'),
      maxLength: 20,
      validator: (String value) {
        if (value.isEmpty) {
          return 'Email is Required';
        } else if (!RegExp(regExp).hasMatch(value)) {
          return 'Please enter a valid name';
        }

        return null;
      },
      onSaved: (String value) {
        _name = value;
      },
      onChanged: (String value) {
        setState(() {
          _name = value;
          if (_name.length == 0) {
            nameFilled = false;
          } else {
            nameFilled = true;
          }
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
        } else if (!RegExp(regExp).hasMatch(value)) {
          return 'Please enter a valid surname';
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
            if (_surname.length == 0) {
              surnameFilled = false;
            } else {
              surnameFilled = true;
            }
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
          Navigator.pushNamed(context, SecondPage.routeName,
              arguments: ScreenArguments(_name, _surname, birthDate,
                  _genderValue, _cityValue, _sideEffectValue, _vaccineTypeValue)
              //MaterialPageRoute(builder: (context) => SecondPage()),
              );
          //Send to API
        },
      ),
    );
  }

  Widget _buildXX() {
    return TextFormField(
      maxLength: 20,
      validator: (String value) {
        if (value.isEmpty) {
          return 'Required';
        } else if (!RegExp(regExp).hasMatch(value)) {
          return 'Please enter a valid input';
        }
        return null;
      },
      onSaved: (String value) {
        _name = value;
      },
      onChanged: (String value) {
        setState(() {
          _name = value;
          if (_name.length == 0) {
            nameFilled = false;
          } else {
            nameFilled = true;
          }
        });
      },
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
                _buildXX(),
                SizedBox(height: 100),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

// things about result page
class ScreenArguments {
  String _name;
  String _surname;
  DateTime birthDate;
  String _cityValue;
  String _genderValue;
  String _vaccineTypeValue;
  String _sideEffectValue;
  ScreenArguments(this._name, this._surname, this.birthDate, this._genderValue,
      this._cityValue, this._sideEffectValue, this._vaccineTypeValue);
}

class SecondPage extends StatelessWidget {
  static const routeName = '/submitResult';
  @override
  Widget build(BuildContext context) {
    // Extract the arguments from the current ModalRoute settings and cast
    // them as ScreenArguments.
    final ScreenArguments args = ModalRoute.of(context).settings.arguments;

    return Scaffold(
        appBar: AppBar(
          title: Text("Form Submitted"),
        ),
        body: Center(
            child: Container(
          child: Column(
            children: [
              Text(args._name),
              Text(args._surname),
              Text(args.birthDate.toString()),
              Text(args._genderValue),
              Text(args._cityValue),
              Text(args._vaccineTypeValue),
              Text(args._sideEffectValue),
              ElevatedButton(
                onPressed: () {
                  // Navigate back to first route when tapped.
                  Navigator.pop(context);
                },
                child: Text('Go back!'),
              ),
            ],
          ),
        )));
  }
}
