package com.company;
import java.awt.*;
import java.io.File;
import org.python.util.PythonInterpreter;
import java.io.*;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import javax.swing.*;
import javax.swing.border.Border;

public class Main {

    // МЕТОД ДЛЯ ПОСЫЛКИ СТРОКИ В ПАЙТОН
    /*
    public static void callPythonScript(String value) {
        try {
            ProcessBuilder processBuilder = new ProcessBuilder("python", "java_test.py", value);
            Process process = processBuilder.start();

            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
            int exitCode = process.waitFor();
            System.out.println("\nPython script exited with code: " + exitCode);

        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }

     */




    public static void main(String[] args){
        // САМО ОКНО
        // python function sneding arguments
        //String value = " some value";
        //callPythonScript(value);

        /*
        PythonInterpreter.initialize(System.getProperties(), System.getProperties(), new String[0]);
        PythonInterpreter interpreter = new PythonInterpreter();
        interpreter.exec("import sys; print(sys.executable)");

         */


        /*
        JFrame frame = new JFrame("Combo Box Example");
        JPanel panel = new JPanel();
        JLabel label = new JLabel();
        JLabel label2 = new JLabel();
        JButton button = new JButton("Start testing");
        button.setLayout(new BorderLayout());
        panel.add(button);
        label.setText("Select strategy: ");
        panel.add(label);
        String[] choices = {"Strategy 1"};
        JComboBox<String> comboBox = new JComboBox<>(choices);
        panel.add(comboBox);
        label2.setText("Select the ticker: ");
        panel.add(label2);
        String[] ticker = {"TSLA", "GOOG", "MSFT"};
        JComboBox<String> comboBox2 = new JComboBox<>(ticker);
        panel.add(comboBox2);

        frame.add(panel);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);
        frame.setSize(575,300 );

         */







	// PYTHON SCRIPT который пойдет в кнопку

        PythonInterpreter pythonInterpreter = new PythonInterpreter();
        String scriptPath = "C:\\Users\\HP\\OneDrive\\Рабочий стол\\PythonProjects\\backtest.py";
        File scriptFile = new File(scriptPath);
        // pythonInterpreter.execfile("script.py");
        if (scriptFile.exists()) {
            // execute the script file
            pythonInterpreter.execfile(scriptPath);
        } else {
            System.err.println("Script file not found: " + scriptPath);
        }






    }
}
