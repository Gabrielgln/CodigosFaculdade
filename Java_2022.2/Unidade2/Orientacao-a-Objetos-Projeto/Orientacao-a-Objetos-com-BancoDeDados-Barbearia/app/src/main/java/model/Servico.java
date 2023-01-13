/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package model;

/**
 *
 * @author gabri
 */
public class Servico {
    
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
