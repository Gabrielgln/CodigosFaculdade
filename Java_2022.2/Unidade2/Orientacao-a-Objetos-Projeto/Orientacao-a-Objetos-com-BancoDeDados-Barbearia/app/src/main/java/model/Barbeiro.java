/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package model;

/**
 *
 * @author gabri
 */
public class Barbeiro {
   
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
  @Override
  public String toString(){
    return "\nBarbeiro: "+nome;
  } 
}
