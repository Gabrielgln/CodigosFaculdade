
class Main {
  public static void main(String[] args) {

    // //Criação do objeto admin
    Admin a1 = new Admin();
    // //Criação do objeto informações que faz a junção das 3 classes:
    Informacoes info = new Informacoes();
    // //Criação do objeto agenda que é um arrayList:
    Agenda agenda = new Agenda();

    // //Criação Objeto Cliente
    Cliente c1 = new Cliente();
    c1.setNome("Gabriel");
    c1.setEmail("gabriellira@007.com"); 
    c1.setTelefone("83987164734");

    Cliente c2 = new Cliente();
    c2.setNome("Gabriel");
    c2.setEmail("elder@007.com"); 
    c2.setTelefone("83987164734");

    
    // //Criação dos objetos barbeiro,serviço e dataHora
    Barbeiro b1 = new Barbeiro("gabriel");
    Barbeiro b2 = new Barbeiro("dois");
    Servico s1 = new Servico("corte");
    DataHora d1 = new DataHora("12/12/2022 - 15:00:00");

    // //Cadastramento dos objetos:

    a1.cadastrarCliente(c1);
    a1.cadastrarCliente(c2);
    
    a1.cadastrarBarbeiro(b1);
    a1.cadastrarBarbeiro(b2);
    a1.cadastrarServico(s1);
    a1.cadastrarDataHora(d1);

    // //Criação do objeto informações com parâmetros dos 3 objetos acima:
    Informacoes info1 = new Informacoes(d1,s1,b1);
    Informacoes info2 = new Informacoes(d1,s1,b2);
    //Criação do objeto agendamento com parâmetros de informações e cliente:
    Agendamento ag2 = new Agendamento(info2,c2);
    Agendamento ag1 = new Agendamento(info1,c1);
    //Função para adicionar o agendamento na agenda:
    agenda.agendarHorario(ag2);
    agenda.agendarHorario(ag1);
    //agenda.agendarHorario(ag3);
    //Função para imprimir o relatorio geral:
    agenda.imprimirRelatorio();
    //Função para imprimir um agendamento especifico:
    //c1.imprimirAgendamentoCliente();
    a1.excluirAgendamento(ag2);
    agenda.imprimirRelatorio();
    
    
    
    

    
    
    // a1.selecionarInformações();
    // a1.imprimir();

    // a1.cadastrarBarbeiro(b2);
    // a1.imprimirBarbeiro();
    // a1.excluirBarbeiro(b1);
    // a1.atualizarBarbeiro(b2);
    // a1.imprimirBarbeiro();
    
    // Cliente c2 = new Cliente();
    // c2.setNome("Elder");
    // c2.setEmail("eldermarquin@007.com"); 
    // c2.setTelefone("83988631845");
    
    // Cliente c3 = new Cliente();
    // c3.setNome("veronica");
    // c3.setEmail("veronica@007.com"); 
    // c3.setTelefone("83996004771");

    // //Adicionando cliente, a lista de clientes
    // a1.cadastrarCliente(c1);
    // a1.cadastrarCliente(c2);
    // a1.cadastrarCliente(c3);

    // //Imprimindo a lista de clientes
    // a1.imprimirCliente();

    // //Criação Objeto Barbeiro
   
    // Barbeiro b2 = new Barbeiro("Elder");

    // //Adicionando barbeiro, a lista de barbeiros
   
    
    // a1.cadastrarBarbeiro(b2);
    
    // //Criação Objeto Servico
    // Servico s1 = new Servico("corte");
    // Servico s2 = new Servico("Sombrancelha");

    // //Adicionando serviço, a lista de serviços
    // a1.cadastrarServico(s1);
    // a1.cadastrarServico(s2);
    
    // //Criação Objeto Data e hora
    // DataHora d1 = new DataHora("14/11/2022-18:00");
    // DataHora d2 = new DataHora("14/11/2022-17:00");

    // //Adicionando datas e horas, a lista de data e horas
    // a1.cadastrarDataHora(d1);
    // a1.cadastrarDataHora(d2);

    // // Selecionando as informações para o agendamento:
    
    // a1.selecionarInformacoes();
    // a1.selecionarInformacoes();
    // a1.imprimir();

    // Informacoes info = new Informacoes();
    // info.imprimir();
    


    
      
    
    
    
  
    
    
  }
}