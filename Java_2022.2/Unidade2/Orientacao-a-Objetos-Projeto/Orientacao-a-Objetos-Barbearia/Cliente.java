public class Cliente extends Pessoa{

  //atributos
  private Agenda agenda;
  private Informacoes info;

  //Construtor:
  public Cliente(){
    super();
    this.agenda = new Agenda();
    this.info = new Informacoes();  
  }

  //Função de agendamento:
  public void selecionarInformacoes(){
    info.selecionarInformacoes();
  }

  //Função para solicitar o cancelamento do agendamento:
  public void solicitarCancelamento(){
    System.out.println("Em desenvolvimento!");
  }

  //Função para imprimir o agendamento de um cliente especifico:
  public void imprimirAgendamentoCliente(){
    info.imprimirAgendamentoCliente();
  }
}
  
