import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { NavbarComponent } from './components/navbar/navbar.component';
import { TopGeneralFeedComponent } from './components/top-general-feed/top-general-feed.component';

import { AuthenticationService } from './services/authentication/authentication.service';

import { TopTargetedFeedComponent } from './components/top-targeted-feed/top-targeted-feed.component';

import { MatButtonModule, MatToolbarModule, MatIconModule, MatMenuModule } from '@angular/material';

import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { library } from '@fortawesome/fontawesome-svg-core';
import { faCoffee } from '@fortawesome/free-solid-svg-icons';
import { CommunitiesComponent } from './components/communities/communities.component';

library.add(faCoffee);

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    TopGeneralFeedComponent,
    TopTargetedFeedComponent,
    CommunitiesComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    MatButtonModule,
    MatToolbarModule,
    MatIconModule,
    FontAwesomeModule,
    MatMenuModule,
    BrowserAnimationsModule
  ],
  providers: [AuthenticationService],
  bootstrap: [AppComponent]
})
export class AppModule { }
