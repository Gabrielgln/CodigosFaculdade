public class Barbeiro{

  //atributos
  private String nome;

  //Construto vazio:
  public Barbeiro(){}

  //Construtor:
  public Barbeiro(String nome){
    this.nome = nome;
  }

  //Acessores:
  public void setNome(String nome){
    this.nome = nome;
  }

  public String getNome(){
    return nome;
  }
  //toString
  public String toString(){
    return "Barbeiro: "+nome;
  }
}