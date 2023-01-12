public class DataHora{

  //atributos
  private String registro;

  //Construtor vazio:
  public DataHora(){}
  
  //Construto:
  public DataHora(String registro){
    this.registro = registro;
  }

  //Acessores:
  public void setRegistro(String registro){
    this.registro = registro;
  }

  public String getRegistro(){
    return registro;
  }

  //toString:
  public String toString(){
    return "\nData Hora: "+registro;
  }
}