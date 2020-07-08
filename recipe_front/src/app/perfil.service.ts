import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { AuthService } from './auth.service';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class PerfilService {

  constructor(private http: HttpClient, private auth$: AuthService) { }

  perfilLogado(){
    return this.http.get(environment.API_URL.concat('perfil-logado/'), this.auth$.httpOptions());
  }
}
