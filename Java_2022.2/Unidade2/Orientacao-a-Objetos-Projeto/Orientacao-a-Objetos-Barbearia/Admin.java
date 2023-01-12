public class Admin extends Pessoa{

  //atributos
  private Agenda agenda;
  private Agendamento agendamento;
  private Informacoes info;

  //Construtor:
  public Admin(){
    super();
    this.agenda = new Agenda();
    this.info = new Informacoes();
  }

  //Função para agendar horario:
  public void selecionarInformacoes(){
    info.selecionarInformacoes();
  }

  //Funções para cadastrar as informações:
  public void cadastrarBarbeiro(Barbeiro nome){
    info.getBarbeiros().add(nome);
  }

  public void cadastrarServico(Servico nome){
    info.getServicos().add(nome);
  }

  public void cadastrarDataHora(DataHora nome){
    info.getDataHoras().add(nome);
  }

  public void cadastrarCliente(Cliente cliente){
    info.getClientes().add(cliente);
  }

  //Funções para deletar as informações:
  public void excluirBarbeiro(Barbeiro nome_barbeiro){
    info.getBarbeiros().remove(nome_barbeiro);
  }

  public void excluirDataHora(DataHora registro_dataHora){
    info.getDataHoras().remove(registro_dataHora);
  }

  public void excluirServico(Servico descricao_servico){
    info.getServicos().remove(descricao_servico);
  }

  public void excluirAgendamento(Agendamento agendamento){
    agenda.getAgendas().remove(agendamento);   
  }
 

  //Funções para atualizar as informações:
  public void atualizarBarbeiro(Barbeiro nome_barbeiro){
    for(Barbeiro barbeiro_lista: info.getBarbeiros()){
      if(barbeiro_lista == nome_barbeiro){
        barbeiro_lista.setNome("elder");
      }
    }
  }

  public void atualizarDataHora(DataHora registro_dataHora){
    for(DataHora dataHora_lista: info.getDataHoras()){
      if(dataHora_lista == registro_dataHora){
        dataHora_lista.setRegistro("12/12/2022 - 10:00:00");
      }
    }
  }

  public void atualizarServico(Servico descricao_servico){
    for(Servico servico_lista: info.getServicos()){
      if(servico_lista == descricao_servico){
        servico_lista.setDescricao("Selagem");
      }
    }
  }

  //Funções para imprimir:
  public void imprimirBarbeiro(){
    info.imprimirBarbeiro();
  }

  public void imprimirServico(){
    info.imprimirServico();
  }

  public void imprimirDataHora(){
    info.imprimirDataHora();
  }

  public void imprimirCliente(){
    for(Cliente cliente : info.getClientes()){
      System.out.println(cliente);
    }
  }

  public void imprimirRelatorio(){
    info.imprimirRelatorio();  
  }

}