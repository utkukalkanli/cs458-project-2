package com.example.cs453_project;

import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AppCompatActivity;

import android.app.AlertDialog;
import android.app.DatePickerDialog;
import android.content.DialogInterface;
import android.icu.util.Calendar;
import android.os.Build;
import android.os.Bundle;
import android.text.Editable;
import android.text.InputFilter;
import android.text.Spanned;
import android.text.TextWatcher;
import android.view.View;
import android.view.Window;
import android.widget.AdapterView;
import android.widget.Button;
import android.widget.DatePicker;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.TextView;

import java.text.MessageFormat;
import java.util.Date;
import java.util.regex.Pattern;

public class MainActivity extends AppCompatActivity implements View.OnClickListener{

    private Button selectDate;
    private DatePickerDialog datePickerDialog;
    private TextView dateTxt;
    private Calendar calendar;
    private int year, month, dayOfMonth;
    EditText nameet,surnameet;
    Spinner cityspn,genderspn,vtypespn,vseffectspn;

    private Button submitBtn;

    private boolean dateFlag, nameFlag, surNameFlag , cityflag, sexflag, vaccflag;

    @RequiresApi(api = Build.VERSION_CODES.O)
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setTitle("Vaccine Survey Page");
        setContentView(R.layout.activity_main);
        Calendar c = Calendar.getInstance();

        cityspn = findViewById(R.id.spinnercity);
        genderspn = findViewById(R.id.spinnersex);
        vtypespn = findViewById(R.id.spinnervaccine);
        vseffectspn = findViewById(R.id.spinnersideeffect);

        nameet = findViewById(R.id.nameedittext);
        surnameet = findViewById(R.id.surnameedittext);
        submitBtn = findViewById(R.id.button);
        submitBtn.setVisibility(View.INVISIBLE);

        selectDate = findViewById(R.id.selectDate);
        dateTxt = findViewById(R.id.dateTxt);
        selectDate.setOnClickListener(new View.OnClickListener() {
            @RequiresApi(api = Build.VERSION_CODES.N)
            @Override
            public void onClick(View view) {
                calendar = Calendar.getInstance();
                year = calendar.get(Calendar.YEAR);
                month = calendar.get(Calendar.MONTH);
                dayOfMonth = calendar.get(Calendar.DAY_OF_MONTH);
                datePickerDialog = new DatePickerDialog(MainActivity.this,
                        new DatePickerDialog.OnDateSetListener() {
                            @Override
                            public void onDateSet(DatePicker datePicker, int year, int month, int day) {
                                dateTxt.setText(day + "/" + (month+1) + "/" + year);
                                dateFlag = true;
                                CheckButton();
                            }
                        }, year, month, dayOfMonth);
                datePickerDialog.getDatePicker().setMaxDate(c.getTimeInMillis());
                datePickerDialog.show();
            }
        });



        nameet.addTextChangedListener(new TextWatcher() {
            CharSequence oldText;
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {

            }

            public void onTextChanged(CharSequence s, int start,
                                      int before, int count) {
            }

            @Override
            public void afterTextChanged(Editable s) {
                if(nameet.length() <= 0){
                    nameFlag = false;
                }else{
                    nameFlag = true;
                }
                CheckButton();
            }
        });

        InputFilter[] filterArray = new InputFilter[2];
        filterArray[0] =
                new InputFilter() {
                    @Override
                    public CharSequence filter(CharSequence cs, int start,
                                               int end, Spanned spanned, int dStart, int dEnd) {
                        // TODO Auto-generated method stub
                        if (cs.equals("")) { // for backspace
                            return cs;
                        }
                        if (cs.toString().matches("[A-Za-z]*")) { // here no space character
                            return cs;
                        }
                        return "";
                    }
                };

        filterArray[1] = new InputFilter.LengthFilter(20);

        nameet.setFilters(filterArray);

        surnameet.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {

            }

            public void onTextChanged(CharSequence s, int start,
                                      int before, int count) {
                if(surnameet.length() <= 0){
                    surNameFlag = false;
                }else{
                    surNameFlag = true;
                }
                CheckButton();
            }

            @Override
            public void afterTextChanged(Editable s) {

            }
        });

        surnameet.setFilters(filterArray);
        submitBtn.setOnClickListener((View.OnClickListener)this);

        cityspn.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> parentView, View selectedItemView, int position, long id) {
                // your code here
                if(id == 0){
                    cityflag = false;
                }else{
                    cityflag = true;
                }
                CheckButton();
            }

            @Override
            public void onNothingSelected(AdapterView<?> parent) {

            }
        });
        genderspn.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> parentView, View selectedItemView, int position, long id) {
                // your code here
                if(id == 0){
                    sexflag = false;
                }else{
                    sexflag = true;
                }
                CheckButton();
            }

            @Override
            public void onNothingSelected(AdapterView<?> parent) {

            }
        });
        vtypespn.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> parentView, View selectedItemView, int position, long id) {
                // your code here
                if(id == 0){
                    vaccflag = false;
                }else{
                    vaccflag = true;
                }
                CheckButton();
            }

            @Override
            public void onNothingSelected(AdapterView<?> parent) {

            }
        });
    }

    private void CheckButton(){
        if(dateFlag && nameFlag && surNameFlag && cityflag && sexflag && vaccflag ){
            System.out.println(vtypespn.getSelectedItem());
            submitBtn.setVisibility(View.VISIBLE);
        }else{
            submitBtn.setVisibility(View.INVISIBLE);
        }
    }

    @Override
    public void onClick(View v) {
        if(v.getId() ==  R.id.button){
            AlertDialog.Builder builder1 = new AlertDialog.Builder(this);
            builder1.setMessage(MessageFormat.format("Name: {0}\nSurname: {1}\nDate: {2}\nCity: {3}\nGender: {4}\nVaccine type: {5}\nVaccine Side-effect: {6}", nameet.getText(),surnameet.getText(),dateTxt.getText(),
                    cityspn.getSelectedItem().toString(),
                    genderspn.getSelectedItem().toString(),
                    vtypespn.getSelectedItem().toString(),
                    vseffectspn.getSelectedItem().toString()));
            builder1.setCancelable(true);

            builder1.setPositiveButton(
                    "OK",
                    new DialogInterface.OnClickListener() {
                        public void onClick(DialogInterface dialog, int id) {
                            dialog.cancel();
                        }
                    });
            AlertDialog alert11 = builder1.create();
            alert11.show();
            selectDate.setEnabled(false);
            nameet.setEnabled(false);
            surnameet.setEnabled(false);
            cityspn.setEnabled(false);
            genderspn.setEnabled(false);
            vtypespn.setEnabled(false);
            vseffectspn.setEnabled(false);
            submitBtn.setVisibility(View.INVISIBLE);
        }
    }
}