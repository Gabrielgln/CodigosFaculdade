public class Agendamento{

  //atributos
  private Informacoes info;
  private Cliente cliente;

  //Construtor vazio
  public Agendamento(){}

  //Construtor:
  public Agendamento(Informacoes info,Cliente cliente){
    this.info = info;
    this.cliente = cliente;
  }

  //Acessores:
  public Cliente getCliente(){
    return cliente;
  }

  public void setCliente(Cliente cliente){
    this.cliente = cliente;
  }

  //Função toString para pegar as informações + cliente:
  public String toString(){
    return "\n-------Registro de agendamento-------\n"+info+
      "\nCliente: "+cliente;
    
  }
}