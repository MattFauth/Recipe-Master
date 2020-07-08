import { Component, OnInit } from '@angular/core';
import { AuthService } from '../auth.service';
import { PerfilService } from '../perfil.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-perfil',
  templateUrl: './perfil.component.html',
  styleUrls: ['./perfil.component.css']
})
export class PerfilComponent implements OnInit {
  user: any;
  perfil: any;
  temPerfil = null;

  constructor(public auth$: AuthService, private perfil$: PerfilService, private router: Router) { }

  ngOnInit(): void {
    this.user = this.auth$.user();
    if(this.user){
      this.perfil$.perfilLogado()
        .subscribe(
          dados => this.perfil = dados,
          erro => this.temPerfil = false
        );
    } else{
      this.router.navigate(['/login']);
    }
  }

  logout(){
    this.auth$.logout();
    this.router.navigate(['/']);
  }

}
