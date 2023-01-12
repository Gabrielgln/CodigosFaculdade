public class Servico{

  //atributos:
  private String descricao;

  //Construtor vazio
  public Servico(){}

  //Construtor:
  public Servico(String descricao){
    this.descricao = descricao;
  }

  //Acessores:
  public void setDescricao(String descricao){
    this.descricao = descricao;
  }

  public String getDescricao(){
    return descricao;
  }

  //toString:
  public String toString(){
    return "\nServiço: "+descricao;
  }
}