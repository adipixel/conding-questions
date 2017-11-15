// Anagram

import java.io.*;
import java.util.Arrays;
import java.util.HashMap;

class myCode
{
    public static void main (String[] args) throws java.lang.Exception
    {
        
        String s1 = "sil ent";
        String s2 = "li,sten";
        
        if (anagram(s1).equals(anagram(s2)))
        {
            System.out.println("Anagram!");
        }
        else
        {
            System.out.println("Mismatch");
        }
    }
    
    public static HashMap<String, Integer> anagram(String s1){
        HashMap<String, Integer> amap = new HashMap<String, Integer>();
        for(int i=0; i<s1.length(); i++)
        {
            if(s1.charAt(i) ==' ' || s1.charAt(i) == ',')
            {
                //
            }
            else
            {
                if (!amap.containsKey(s1.charAt(i)+""))
                {
                    amap.put(s1.charAt(i)+"", 1);
                }
                else
                {
                    amap.put(s1.charAt(i)+"", amap.get(s1.charAt(i))+1);
                }                
            }

        }
        return amap;
    }
}
