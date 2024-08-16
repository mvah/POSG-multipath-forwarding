import interfaces.IElement;

import java.util.ArrayList;
import java.util.List;

public class File<T> {
    private List<T> valueList = new ArrayList<T>();

    public void enfiler(T value) {
        this.valueList.add(value);
    }

    public T defiler(){
        if(this.valueList.isEmpty()){
            return null;
        }
        return valueList.remove(0);
    }

    public boolean estVide(){
        return valueList.isEmpty();
    }
}
