import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
        private static String special_characters = "!@#$%^&*()-+";
    static int minimumNumber(int n, String password) {
        // Return the minimum number of characters to make the password strong
        int num=0, lc=0, uc=0, sc=0;
        int mainCounter = 0;
        for(char ch: password.toCharArray()){
            int ascii = (int)ch;
            if(special_characters.contains(ch+"")){
                sc++;
                if(sc == 1){
                    mainCounter++;
                }
            }
            else if(ascii >= 48 && ascii <= 57){
                num++;
                if(num == 1){
                    mainCounter++;
                }
                
            }
            else if(ascii >= 65 && ascii <= 90){
                uc++;
                if(uc == 1){
                    mainCounter++;
                }
            }
            else if(ascii >= 97 && ascii <= 122){
                lc++;
                if(lc == 1){
                    mainCounter++;
                }
            }
            
            if(mainCounter == 4)
            {
                break;
            }
        }
        
        if (password.length() >= 6){
            if (mainCounter == 4){
                return 0;
            }
            else{
                return 4-mainCounter;
            }
        }
        else{
            if(mainCounter == 4){
                return (6 - password.length());
            }
            else{
                if(password.length()+(4-mainCounter) >= 6){
                    return ((4-mainCounter));
                }
                else{
                    return (6-(password.length()+(4-mainCounter)))+(4-mainCounter);
                }
            }
        }
        
        
        
        
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        String password = in.next();
        int answer = minimumNumber(n, password);
        System.out.println(answer);
        in.close();
    }
}
