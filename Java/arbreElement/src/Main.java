import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import java.io.PrintWriter;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        Integer v = Integer.valueOf(args[0]);
        Element element = traiter2(new Element(generateRandomString(v)));
        //affichage(element);
    }

    /*public static Element traiter(Element element){
        List<String> result = GenerationArbre.generate(element);

        for (String s : result) {
            Element newElement = new Element(s);
            traiter(newElement);
            element.getElementList().add(newElement);
        }
        return element;
    }*/

    public static Element traiter2(Element element){
        long startTime = System.nanoTime();
        try {
            PrintWriter writer = new PrintWriter("output.txt");
            File<Element> file = new File<>();
            file.enfiler(element);
            System.out.print("{");
            writer.print("{");
            List<String> chaineList = new ArrayList<>();
            while (!file.estVide()){
                Element elmt = file.defiler();
                if(elmt.getTaille()>=1 && !chaineList.contains(elmt.getValue())){
                    List<String> result = GenerationArbre.generate(elmt);
                    chaineList.add(elmt.getValue());
                    writer.print("\""+elmt.getValue()+"\": [");
                    System.out.print(" "+elmt.getValue()+" : [");
                    int i=0;

                    for (String str: result){
                        i++;
                        writer.print("\""+str+"\"");
                        System.out.print(" "+str);
                        if(i!=result.size()){
                            writer.print(",");
                            System.out.print(",");
                        }
                        Element newElement = new Element(str);
                        elmt.getElementList().add(newElement);
                        file.enfiler(newElement);
                    }
                    writer.print("],");
                    System.out.print("],");
                }
            }
            writer.print("}");
            System.out.print("}");
            long endTime = System.nanoTime();
            long duration = (endTime - startTime)/1000000;
            writer.print("\nDuration " +duration+" ms");
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return element;
    }

    public static void affichage(Element element){
        File<Element> file = new File<>();
        file.enfiler(element);
        List<String> chaineList = new ArrayList<>();
        System.out.print("\"{ ");
        while (!file.estVide()){
            Element elementDefiler = file.defiler();
            if(elementDefiler.getTaille()>=1 && !chaineList.contains(elementDefiler.getValue())){
                chaineList.add(elementDefiler.getValue());
                System.out.print("'"+ elementDefiler.getValue()+"' : [");
                int i = 0;
                for(Element elmt : elementDefiler.getElementList()){
                    i++;
                    file.enfiler(elmt);
                    System.out.print(" ' "+elmt.getValue());
                    if(i!=elementDefiler.getElementList().size()){
                        System.out.print(",");
                    }
                }
                System.out.print(" ], ");
            }

        }
        System.out.println(" }");

    }
    public static String generateRandomString(int length) {
        String characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
        StringBuilder sb = new StringBuilder(length);
        Random random = new Random();

        for (int i = 0; i < length; i++) {
            int randomIndex = random.nextInt(characters.length());
            char randomChar = characters.charAt(randomIndex);
            sb.append(randomChar);
        }

        return sb.toString();
    }}