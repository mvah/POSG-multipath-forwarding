import interfaces.IElement;

import java.util.ArrayList;
import java.util.List;

public class Element implements IElement {

    private String value;
    private List<Element> elementList = new ArrayList<Element>();

    private Integer taille;

    public Element(String value) {
        this.value = value;
        taille = value.length();
    }

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
        taille = value.length();
    }

    public List<Element> getElementList() {
        return elementList;
    }

    public void setElementList(List<Element> elementList) {
        this.elementList = elementList;
    }

    public Integer getTaille() {
        return taille;
    }

    @Override
    public String toString() {
        return "Element{" +
                "value='" + value + '\'' +
                ", elementList=" + elementList +
                '}';
    }
}
