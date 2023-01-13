/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package main;

import controller.AgendamentoController;
import controller.BarbeiroController;
import controller.ClienteController;
import controller.DataHoraController;
import controller.ServicoController;
import model.Agendamento;
import model.Barbeiro;
import model.Cliente;
import model.DataHora;
import model.Servico;

/**
 *
 * @author gabri
 */
public class Main {
    
    public static void main(String[]args){
        
        //cliente
        ClienteController clienteController = new ClienteController();
        Cliente cliente = new Cliente();
        cliente.setNome("Gabriel");
        cliente.setEmail("gabrielescamoso@gmail.com");
        cliente.setTelefone("00920922");
        
        clienteController.save(cliente);
        
        //barbeiro
        BarbeiroController barbeiroController = new BarbeiroController();
        Barbeiro barbeiro = new Barbeiro();
        barbeiro.setNome("Joao");
        
        barbeiroController.save(barbeiro);
        
        //servico
        ServicoController servicoController = new ServicoController();
        Servico servico = new Servico();
        servico.setDescricao("Corte");
        
        servicoController.save(servico);
        
        //dataHora
        DataHoraController dataHoraController = new DataHoraController();
        DataHora dataHora = new DataHora();
        dataHora.setRegistro("16/11/2022-18:00");
        
        dataHoraController.save(dataHora);
        
        //agendamento
        AgendamentoController agendamentoController = new AgendamentoController();
        Agendamento agendamento = new Agendamento();
        agendamento.setBarbeiroNome("Joao");
        agendamento.setClienteEmail("gabrielescamoso@gmail.com");
        agendamento.setServicoDescricao("Corte");
        agendamento.setDataHoraRegistro("16/11/2022-18:00");
        
        agendamentoController.save(agendamento);
        
        
        

    }
}
