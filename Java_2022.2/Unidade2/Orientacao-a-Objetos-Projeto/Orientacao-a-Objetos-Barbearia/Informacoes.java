import java.util.ArrayList;
import java.util.Scanner;

public class Informacoes{

  //atributos - Junção das 3 classes:
  private DataHora dataHora;
  private Servico servico;
  private Barbeiro barbeiro;
  
  //Para ter acesso a agenda, sempre tem que inicializar ela!
  private Agenda agenda = new Agenda();

  //Criando lista para cada classe:
  private static ArrayList<Barbeiro> barbeiros = new ArrayList<>();
  private static ArrayList<Servico> servicos = new ArrayList<>();
  private static ArrayList<DataHora> dataHoras = new ArrayList<>();
  private static ArrayList<Cliente> clientes = new ArrayList<>();

  //Scanner para ler informações:
  Scanner leitor = new Scanner(System.in);

  //Construtor vazio:
  public Informacoes(){}

  //Construtor:
  public Informacoes(DataHora dataHora, Servico servico, Barbeiro barbeiro){
    this.dataHora = dataHora;
    this.servico = servico;
    this.barbeiro = barbeiro; 
  }
  
  //Função completa para agendamento de horario:
  public void selecionarInformacoes(){ 

    //iniciando os objetos para incrementar com o leitor:
    Barbeiro barbeiro_cliente = new Barbeiro();
    Servico servico_cliente = new Servico();
    DataHora dataHora_cliente = new DataHora();
    Cliente cliente_cliente = new Cliente();
    
    this.imprimirBarbeiro();
    System.out.println("Digite o barbeiro que deseja: ");
    barbeiro_cliente.setNome(leitor.nextLine());
    
    for(Barbeiro aux_barbeiro: barbeiros){
      if(barbeiro_cliente.getNome().equals(aux_barbeiro.getNome())){

        this.imprimirServico();
        System.out.println("Digite o servico que deseja: ");
        servico_cliente.setDescricao(leitor.nextLine());
        
        for(Servico aux_servico: servicos){
          if(aux_servico.getDescricao().equals(servico_cliente.getDescricao())){
            
            this.imprimirDataHora();
            System.out.println("Digite a data e hora que deseja que deseja: ");
            dataHora_cliente.setRegistro(leitor.nextLine());
            
            for(DataHora aux_dataHora: dataHoras){
              if(aux_dataHora.getRegistro().equals(dataHora_cliente.getRegistro())){
                
                System.out.println("Digite o seu email para confirmação do agendamento: ");
                cliente_cliente.setEmail(leitor.nextLine());
                for(Cliente aux_cliente: clientes){
                  if(aux_cliente.getEmail().equals(cliente_cliente.getEmail())){
                    Informacoes info = new Informacoes(dataHora_cliente,servico_cliente,barbeiro_cliente);
                    Agendamento ag = new Agendamento(info,aux_cliente);
                    agenda.agendarHorario(ag);
                    System.out.println("Agendamento realizado com sucesso!");
                  }
                }
                //falta implementar as exceções de "Não encontrado!"
                //System.out.println("Cliente não encotrado, tente novamente!");
                //this.selecionarInformacoes();
              }
            }
            //System.out.println("Horario não correspondente, tente novamente!");
            //this.selecionarInformacoes();
          }
        }
        //System.out.println("Serviço não correspondente, tente novamente!");
        //this.selecionarInformacoes();
      }  
    }
    //System.out.println("Barbeiro não correspondente, tente novamente!");
    //this.selecionarInformacoes();
  }

  //Funções para visualizar:
  public void imprimirBarbeiro(){
    for(Barbeiro aux_barbeiro : barbeiros){
      System.out.println(aux_barbeiro);
    }
  }

  public void imprimirServico(){
    for(Servico aux_servico : servicos){
      System.out.println(aux_servico);
    }
  }

  public void imprimirDataHora(){
    for(DataHora aux_dataHora : dataHoras){
      System.out.println(aux_dataHora);
    }
  }

  public void imprimirRelatorio(){
    agenda.imprimirRelatorio();
  }

  public void imprimirAgendamentoCliente(){
    agenda.imprimirAgendamentoCliente();
  }

  //Acessores - get:
  public ArrayList<Barbeiro> getBarbeiros(){
    return barbeiros;
  }

  public ArrayList<Servico> getServicos(){
    return servicos;
  }

  public ArrayList<DataHora> getDataHoras(){
    return dataHoras;
  }
  
  public ArrayList<Cliente> getClientes(){
    return clientes;
  }
  
  //toString:
  @Override
  public String toString(){
    return "\nInformações: \n"+barbeiro+servico+dataHora;
  }
}