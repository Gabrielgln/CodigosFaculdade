/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package model;

/**
 *
 * @author gabri
 */
public class Agendamento {
    
  private String barbeiroNome;
  private String servicoDescricao;
  private String dataHoraRegistro;
  private String clienteEmail;

  //Construtor vazio
  public Agendamento(){}

  //Construtor:
  public Agendamento(String barbeiroNome, String servicoDescricao, String dataHoraRegistro, String clienteEmail){
    this.barbeiroNome = barbeiroNome;
    this.servicoDescricao = servicoDescricao;
    this.dataHoraRegistro = dataHoraRegistro;
    this.clienteEmail = clienteEmail;
  }

    public String getBarbeiroNome() {
        return barbeiroNome;
    }

    public void setBarbeiroNome(String barbeiroNome) {
        this.barbeiroNome = barbeiroNome;
    }

    public String getServicoDescricao() {
        return servicoDescricao;
    }

    public void setServicoDescricao(String servicoDescricao) {
        this.servicoDescricao = servicoDescricao;
    }

    public String getDataHoraRegistro() {
        return dataHoraRegistro;
    }

    public void setDataHoraRegistro(String dataHoraRegistro) {
        this.dataHoraRegistro = dataHoraRegistro;
    }

    public String getClienteEmail() {
        return clienteEmail;
    }

    public void setClienteEmail(String clienteEmail) {
        this.clienteEmail = clienteEmail;
    }
  
  

  //Função toString para pegar as informações + cliente:
  public String toString(){
    return "\n-------Registro de agendamento-------\n"+barbeiroNome+servicoDescricao+dataHoraRegistro+
      "\nCliente: "+clienteEmail;
    
  }
}
