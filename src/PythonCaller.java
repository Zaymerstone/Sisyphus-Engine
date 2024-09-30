/*


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class PythonCaller {
    public static void callPythonScript(String value) {
        try {
            ProcessBuilder processBuilder = new ProcessBuilder("python", "myscript.py", value);
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

}
*/
